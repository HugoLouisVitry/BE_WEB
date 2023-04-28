-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : ven. 28 avr. 2023 à 15:10
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
  `idUser` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `user`
--

CREATE TABLE `user` (
  `idUser` int(11) NOT NULL,
  `login` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `isAdmin` tinyint(1) DEFAULT NULL,
  `nom` varchar(20) DEFAULT NULL,
  `prenom` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Déchargement des données de la table `user`
--

INSERT INTO `user` (`idUser`, `login`, `password`, `isAdmin`, `nom`, `prenom`) VALUES
(1, 'huyghema', 'huyghema', 1, 'Huyghe', 'Mathias'),
(2, 'lecarpma', 'lecarpma', 1, 'Le Carpentier', 'Marie'),
(3, 'rummenspa', 'rummenspa', 1, 'Rummens', 'Paul'),
(4, 'vitryhu', 'vitryhu', 1, 'Vitry', 'Hugo');

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
  MODIFY `idProject` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `user`
--
ALTER TABLE `user`
  MODIFY `idUser` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

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
