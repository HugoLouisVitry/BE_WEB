-- phpMyAdmin SQL Dump
-- version 5.1.1deb5ubuntu1
-- https://www.phpmyadmin.net/
--
-- Hôte : localhost:3306
-- Généré le : mer. 07 juin 2023 à 17:20
-- Version du serveur : 8.0.33-0ubuntu0.22.04.2
-- Version de PHP : 8.1.2-1ubuntu2.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `financement`
--
CREATE DATABASE IF NOT EXISTS `financement` DEFAULT CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci;
USE `financement`;

-- --------------------------------------------------------

--
-- Structure de la table `participate`
--

CREATE TABLE `participate` (
  `idUser` int NOT NULL,
  `idProject` int NOT NULL,
  `somme` int NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Déchargement des données de la table `participate`
--

INSERT INTO `participate` (`idUser`, `idProject`, `somme`) VALUES
(2, 2, 500),
(2, 8, 14);

-- --------------------------------------------------------

--
-- Structure de la table `project`
--

CREATE TABLE `project` (
  `idProject` int NOT NULL,
  `name` varchar(60) NOT NULL,
  `description` text NOT NULL,
  `target` int NOT NULL,
  `endDate` date NOT NULL,
  `isOpen` tinyint(1) NOT NULL,
  `idUser` int NOT NULL,
  `picture` varchar(60) DEFAULT 'default_picture.png',
  `current` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Déchargement des données de la table `project`
--

INSERT INTO `project` (`idProject`, `name`, `description`, `target`, `endDate`, `isOpen`, `idUser`, `picture`, `current`) VALUES
(1, 'Sauver le groupe huyghe_lecarpentier_vitry_rummens', 'Le groupe se noie sous les projets de BE. Alors que Hugo nous a quittés pour remporter haut la main la Coupe de Robotique, Paul est perdu dans les recoins les plus sombres de Blériot.', 1000000, '2023-07-29', 0, 2, 'default_picture.png', 5000),
(2, 'Goûter', 'Prendre un goûter savoureux chez Mathias', 1000000, '2023-05-23', 1, 2, 'default_picture.png', 10),
(3, 'test', 'test', 1, '2023-05-23', 0, 2, 'default_picture.png', 1),
(4, 'test2', 'test2', 50, '2023-06-22', 0, 2, 'default_picture.png', 22),
(8, 'Perry l\'Ornithorynque (Agent P)', 'Perry est l\'animal de compagnie des deux frères. Même sous la forme d\'un ornithorynque ordinaire, Perry est aussi un des agents secrets de l\'organisation gouvernementale de tout-animal appelée l\'O.W.C.A., et est chargé d\'arrêter le savant \"maléfique\"Heinz Doofenshmirtz. Dès qu\'un des personnages de la série se demande : \"Il est où Perry ?\", il est alors vu dans son \"Q.G.\". Perry revient généralement à la fin de l\'épisode. Phinéas (ou quelqu\'un d\'autre) dit alors : \"Ah, te v\'là, Perry !\". Il ne sait dire que \"RrrrRrr\" (des r roulés) ce qui ne veut absolument rien dire même dans notre langue car malgré un traducteur entre les animaux et les humains construits par Phinéas, il est incapable de faire entendre autre chose que ce bruit. Il devient un cyborg obéissant aux ordres de Doofenshmirtz mais l\'agent M à sauver l\'agent P l\'agent M c\'est Mariama dans une autre dimension dans le film \"Phineas et ferb voyagent dans la 2ème dimension \". ', 2007, '2024-01-01', 1, 4, 'AgentP.png', 1007);

-- --------------------------------------------------------

--
-- Structure de la table `user`
--

CREATE TABLE `user` (
  `idUser` int NOT NULL,
  `login` varchar(20) NOT NULL,
  `password` varchar(90) NOT NULL,
  `isAdmin` tinyint(1) DEFAULT NULL,
  `nom` varchar(20) DEFAULT NULL,
  `prenom` varchar(20) DEFAULT NULL,
  `reponse` varchar(40) DEFAULT NULL,
  `mail` varchar(40) DEFAULT NULL,
  `avatar` varchar(60) NOT NULL DEFAULT 'static/images/avatar/default_user.png',
  `solde` int NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Déchargement des données de la table `user`
--

INSERT INTO `user` (`idUser`, `login`, `password`, `isAdmin`, `nom`, `prenom`, `reponse`, `mail`, `avatar`, `solde`) VALUES
(1, 'huyghema', '203ed44b778fa1a55ffd9cf3dc4407c710a787625d5f2cf365a4e3ad9232fa3f', 1, 'Huyghe', 'Mathias', NULL, 'mathias.huyghe@alumni.enac.fr', 'default_user.png', 500),
(2, 'lecarpma', '1ee3bcb7aff31f0e8d12da84deaf85b1a471731d4ed334189954e52c4b5fcdc1', 1, 'Le Carpentier', 'Marie', NULL, 'marie.le-carpentier@alumni.enac.fr', 'default_user.png', 500),
(3, 'rummenspa', '6f73aaf7bffa8141aa7c7607566063bbcf9993a1efdf79c94a9ba3ad2187595a', 1, 'Rummens', 'Paul', NULL, 'paul.rummens@alumni.enac.fr', 'default_user.png', 5700),
(4, 'vitryhu', 'ec1a405c52aee12ec05e9785d83d89b9fdc1adad1fbe38f7c7904e3e09f6686e', 1, 'Vitry', 'Hugo', NULL, 'hugo.vitry@alumni.enac.fr', 'default_user.png', 1000);

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `participate`
--
ALTER TABLE `participate`
  ADD PRIMARY KEY (`idUser`,`idProject`),
  ADD KEY `participate_project` (`idProject`);

--
-- Index pour la table `project`
--
ALTER TABLE `project`
  ADD PRIMARY KEY (`idProject`),
  ADD KEY `user_foreignkey` (`idUser`);

--
-- Index pour la table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`idUser`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `project`
--
ALTER TABLE `project`
  MODIFY `idProject` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT pour la table `user`
--
ALTER TABLE `user`
  MODIFY `idUser` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `participate`
--
ALTER TABLE `participate`
  ADD CONSTRAINT `participate_project` FOREIGN KEY (`idProject`) REFERENCES `project` (`idProject`),
  ADD CONSTRAINT `participate_user` FOREIGN KEY (`idUser`) REFERENCES `user` (`idUser`);

--
-- Contraintes pour la table `project`
--
ALTER TABLE `project`
  ADD CONSTRAINT `user_foreignkey` FOREIGN KEY (`idUser`) REFERENCES `user` (`idUser`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
