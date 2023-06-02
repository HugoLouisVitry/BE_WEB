-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : ven. 02 juin 2023 à 09:31
-- Version du serveur : 10.4.28-MariaDB
-- Version de PHP : 8.2.4

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
CREATE DATABASE IF NOT EXISTS `financement` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `financement`;

-- --------------------------------------------------------

--
-- Structure de la table `participate`
--

CREATE TABLE `participate` (
  `idUser` int(11) NOT NULL,
  `idProject` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `project`
--

CREATE TABLE `project` (
  `idProject` int(11) NOT NULL,
  `name` varchar(60) NOT NULL,
  `description` text NOT NULL,
  `target` int(11) NOT NULL,
  `endDate` date NOT NULL,
  `isOpen` tinyint(1) NOT NULL,
  `idUser` int(11) NOT NULL,
  `picture` varchar(60) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Déchargement des données de la table `project`
--

INSERT INTO `project` (`idProject`, `name`, `description`, `target`, `endDate`, `isOpen`, `idUser`, `picture`) VALUES
(1, 'Sauver le groupe huyghe_lecarpentier_vitry_rummens', 'Le groupe se noie sous les projets de BE. Alors que Hugo nous a quittés pour remporter haut la main la Coupe de Robotique, Paul est perdu dans les recoins les plus sombres de Blériot.', 1000000, '2023-07-29', 1, 2, 'static/images/default_picture.png'),
(2, 'Goûter', 'Prendre un goûter savoureux chez Mathias', 1000000, '2023-05-23', 1, 2, 'static/images/default_picture.png'),
(3, 'test', 'test', 1, '2023-05-23', 0, 2, 'static/images/default_picture.png'),
(4, 'test2', 'test2', 50, '2023-06-22', 0, 2, 'static/images/default_picture.png');

-- --------------------------------------------------------

--
-- Structure de la table `user`
--

CREATE TABLE `user` (
  `idUser` int(11) NOT NULL,
  `login` varchar(20) NOT NULL,
  `password` varchar(90) NOT NULL,
  `isAdmin` tinyint(1) DEFAULT NULL,
  `nom` varchar(20) DEFAULT NULL,
  `prenom` varchar(20) DEFAULT NULL,
  `reponse` varchar(40) DEFAULT NULL,
  `mail` varchar(40) DEFAULT NULL,
  `avatar` varchar(60) NOT NULL DEFAULT 'static/images/avatar/default_user.png'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Déchargement des données de la table `user`
--

INSERT INTO `user` (`idUser`, `login`, `password`, `isAdmin`, `nom`, `prenom`, `reponse`, `mail`, `avatar`) VALUES
(1, 'huyghema', '203ed44b778fa1a55ffd9cf3dc4407c710a787625d5f2cf365a4e3ad9232fa3f', 1, 'Huyghe', 'Mathias', NULL, 'mathias.huyghe@alumni.enac.fr', 'default_user.png'),
(2, 'lecarpma', '1ee3bcb7aff31f0e8d12da84deaf85b1a471731d4ed334189954e52c4b5fcdc1', 1, 'Le Carpentier', 'Marie', NULL, 'marie.le-carpentier@alumni.enac.fr', 'default_user.png'),
(3, 'rummenspa', '6f73aaf7bffa8141aa7c7607566063bbcf9993a1efdf79c94a9ba3ad2187595a', 1, 'Rummens', 'Paul', NULL, 'paul.rummens@alumni.enac.fr', 'default_user.png'),
(4, 'vitryhu', 'ec1a405c52aee12ec05e9785d83d89b9fdc1adad1fbe38f7c7904e3e09f6686e', 1, 'Vitry', 'Hugo', NULL, 'hugo.vitry@alumni.enac.fr', 'default_user.png');

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
  MODIFY `idProject` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT pour la table `user`
--
ALTER TABLE `user`
  MODIFY `idUser` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

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
