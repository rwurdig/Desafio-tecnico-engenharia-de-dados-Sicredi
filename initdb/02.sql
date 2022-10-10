USE `SICOOPERATIVE`;

-- SICOOPERATIVE.associado definition

CREATE TABLE `associado` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) NOT NULL,
  `sobrenome` varchar(100) NOT NULL,
  `idade` int DEFAULT NULL,
  `email` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=501 DEFAULT CHARSET=utf8mb4;


-- SICOOPERATIVE.conta definition

CREATE TABLE `conta` (
  `id` int NOT NULL AUTO_INCREMENT,
  `tipo` varchar(10) NOT NULL,
  `data_criacao` timestamp NOT NULL,
  `id_associado` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `dim_conta_FK` (`id_associado`),
  CONSTRAINT `dim_conta_FK` FOREIGN KEY (`id_associado`) REFERENCES `associado` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=501 DEFAULT CHARSET=utf8mb4;

-- SICOOPERATIVE.cartao definition

CREATE TABLE `cartao` (
  `id` int NOT NULL AUTO_INCREMENT,
  `num_cartao` bigint NOT NULL,
  `nom_impresso` varchar(100) NOT NULL,
  `id_conta` int DEFAULT NULL,
  `id_associado` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `dim_cartao_FK` (`id_conta`),
  KEY `dim_cartao_FK_1` (`id_associado`),
  CONSTRAINT `dim_cartao_FK` FOREIGN KEY (`id_conta`) REFERENCES `conta` (`id`),
  CONSTRAINT `dim_cartao_FK_1` FOREIGN KEY (`id_associado`) REFERENCES `associado` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1001 DEFAULT CHARSET=utf8mb4;

-- SICOOPERATIVE.movimento definition

CREATE TABLE `movimento` (
  `id` int NOT NULL AUTO_INCREMENT,
  `vlr_transacao` decimal(10,2) NOT NULL,
  `des_transacao` varchar(100) NOT NULL,
  `data_movimento` timestamp NOT NULL,
  `id_cartao` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fat_movimento_FK` (`id_cartao`),
  CONSTRAINT `fat_movimento_FK` FOREIGN KEY (`id_cartao`) REFERENCES `cartao` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=501 DEFAULT CHARSET=utf8mb4;