from sys import argv
from pyspark.sql import DataFrameReader
from utils import get_spark_session
##from pyspark.sql.types import StructType, DoubleType, IntegerType, StringType, TimestampType

class ETLSiCooperative():
    def __init__(self, user:str, password:str, loc_persist:list) -> None:
        self.user = user
        self.password = password
        self.spark_session = get_spark_session()
        if len(loc_persist) > 1 :
            self.loc_persist = loc_persist[1]
        else:
            self.loc_persist = '.'


    def ExtractTables(self, table:str) -> DataFrameReader:
        spark_read = self.spark_session.read.format('jdbc') \
                    .option('url', 'jdbc:mysql://172.20.0.10/SICOOPERATIVE') \
                    .option('driver', 'com.mysql.cj.jdbc.Driver') \
                    .option('dbtable', table) \
                    .option('user', self.user) \
                    .option('password', self.password)

        return spark_read

    def LoadDFTables(self) -> None:
        self.associado = self.ExtractTables('associado').load()
        self.conta = self.ExtractTables('conta').load()
        self.cartao = self.ExtractTables('cartao').load()
        self.movimento = self.ExtractTables('movimento').load()

    def JoinDFTables(self) -> None:
        self.result = self.movimento \
                .join(self.cartao).filter(self.movimento['id_cartao']==self.cartao['id']) \
                .join(self.conta).filter(self.cartao['id_conta']==self.conta['id']) \
                .join(self.associado).filter(self.conta['id_associado']==self.associado['id']) \
                .selectExpr('nome as nome_associado'
                    , 'sobrenome as sobrenome_associado'
                    , 'idade as idade_associado'
                    , 'vlr_transacao as vlr_transacao_movimento'
                    , 'des_transacao as des_transacao_movimento'
                    , 'data_movimento'
                    , 'num_cartao as numero_cartao'
                    , 'nom_impresso as nome_impresso_cartao'
                    , 'data_criacao as data_criacao_cartao'
                    , 'tipo as tipo_conta'
                    , 'data_criacao as data_criacao_conta')
    
    def ModelAndPersistResult(self) -> None:
        """"
        self.result.coalesce(1).write \
            .format('csv') \
            .mode('overwrite') \
            .option('header','true') \
            .option('encoding','UTF-8') \
            .save('{}'.format(self.loc_persist))
        """
        self.result.toPandas().to_csv('dados_movimento.csv', index=False, encoding='UTF-8')

    def runner(self) -> None:
        self.LoadDFTables()
        self.JoinDFTables()
        self.ModelAndPersistResult()

if __name__=='__main__':
    etl = ETLSiCooperative'root','1234', argv)
    etl.runner()