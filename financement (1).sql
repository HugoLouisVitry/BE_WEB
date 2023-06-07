-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : mer. 07 juin 2023 à 19:06
-- Version du serveur : 10.4.27-MariaDB
-- Version de PHP : 8.2.0

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
  `idProject` int(11) NOT NULL,
  `somme` int(11) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Déchargement des données de la table `participate`
--

INSERT INTO `participate` (`idUser`, `idProject`, `somme`) VALUES
(1, 1, 10525),
(2, 2, 500),
(2, 8, 14);

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
  `picture` varchar(60) DEFAULT 'default_picture.png',
  `current` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Déchargement des données de la table `project`
--

INSERT INTO `project` (`idProject`, `name`, `description`, `target`, `endDate`, `isOpen`, `idUser`, `picture`, `current`) VALUES
(1, 'Sauver le groupe huyghe_lecarpentier_vitry_rummens', 'Le groupe se noie sous les projets de BE. Alors que Hugo nous a quittés pour remporter haut la main la Coupe de Robotique, Paul est perdu dans les recoins les plus sombres de Blériot.', 1000000, '2023-07-29', 0, 2, 'default_picture.png', 15525),
(2, 'Goûter', 'Prendre un goûter savoureux chez Mathias', 1000000, '2023-05-23', 1, 2, 'default_picture.png', 10),
(3, 'test', 'test', 1, '2023-05-23', 0, 2, 'default_picture.png', 1),
(4, 'test2', 'test2', 50, '2023-06-22', 0, 2, 'default_picture.png', 22),
(8, 'Perry l\'Ornithorynque (Agent P)', 'Perry est l\'animal de compagnie des deux frères. Même sous la forme d\'un ornithorynque ordinaire, Perry est aussi un des agents secrets de l\'organisation gouvernementale de tout-animal appelée l\'O.W.C.A., et est chargé d\'arrêter le savant \"maléfique\"Heinz Doofenshmirtz. Dès qu\'un des personnages de la série se demande : \"Il est où Perry ?\", il est alors vu dans son \"Q.G.\". Perry revient généralement à la fin de l\'épisode. Phinéas (ou quelqu\'un d\'autre) dit alors : \"Ah, te v\'là, Perry !\". Il ne sait dire que \"RrrrRrr\" (des r roulés) ce qui ne veut absolument rien dire même dans notre langue car malgré un traducteur entre les animaux et les humains construits par Phinéas, il est incapable de faire entendre autre chose que ce bruit. Il devient un cyborg obéissant aux ordres de Doofenshmirtz mais l\'agent M à sauver l\'agent P l\'agent M c\'est Mariama dans une autre dimension dans le film \"Phineas et ferb voyagent dans la 2ème dimension \". ', 2007, '2024-01-01', 1, 4, 'AgentP.png', 1007),
(15, 'Projet A', 'Ce projet a pour ambition de créer une plateforme de réservation en ligne pour les restaurants, simplifiant ainsi le processus de réservation pour les clients..', 1014, '2024-03-22', 1, 2, 'default_picture.png', NULL),
(16, 'Projet B', 'Nous cherchons à concevoir une plateforme d\'échange de livres en ligne, permettant aux utilisateurs de partager, échanger et emprunter des livres..', 9193, '2024-01-09', 1, 3, 'default_picture.png', NULL),
(17, 'Projet C', 'Nous souhaitons concevoir un système de suivi de la condition physique qui permettra aux utilisateurs de suivre leurs progrès et d\'atteindre leurs objectifs de remise en forme..', 7774, '2025-03-17', 1, 4, 'default_picture.png', NULL),
(18, 'Projet D', 'Nous envisageons de développer un outil de gestion de projet collaboratif qui permettra aux équipes de travailler efficacement ensemble, en simplifiant la communication et le suivi des tâches..', 8170, '2024-04-21', 1, 8, 'default_picture.png', NULL),
(19, 'Projet E', 'Nous envisageons de développer une application de suivi des habitudes pour aider les utilisateurs à adopter de nouvelles habitudes et à atteindre leurs objectifs personnels..', 4678, '2023-12-21', 1, 9, 'default_picture.png', NULL),
(20, 'Projet F', 'Nous souhaitons développer un système de recommandation de films personnalisé, offrant aux utilisateurs des suggestions basées sur leurs préférences et leurs historiques..', 8582, '2025-07-08', 1, 10, 'default_picture.png', NULL),
(21, 'Projet G', 'Le projet vise à créer une application de suivi des dépenses personnelles pour aider les utilisateurs à gérer leur budget de manière efficace..', 4471, '2025-08-29', 1, 11, 'default_picture.png', NULL),
(22, 'Projet H', 'Nous cherchons à concevoir un système de gestion de stock automatisé pour les entreprises, facilitant ainsi le suivi des stocks et la gestion des commandes..', 4281, '2025-02-07', 1, 12, 'default_picture.png', NULL),
(23, 'Projet I', 'Nous souhaitons développer un système de réservation en ligne pour les salles de sport, permettant aux utilisateurs de réserver des cours et des équipements..', 7565, '2025-04-06', 1, 13, 'default_picture.png', NULL),
(24, 'Projet J', 'Ce projet a pour ambition de créer une plateforme de réservation en ligne pour les restaurants, simplifiant ainsi le processus de réservation pour les clients..', 8456, '2025-10-30', 1, 14, 'default_picture.png', NULL);

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
  `avatar` varchar(60) NOT NULL DEFAULT 'static/images/avatar/default_user.png',
  `solde` int(11) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Déchargement des données de la table `user`
--

INSERT INTO `user` (`idUser`, `login`, `password`, `isAdmin`, `nom`, `prenom`, `reponse`, `mail`, `avatar`, `solde`) VALUES
(1, 'huyghema', '203ed44b778fa1a55ffd9cf3dc4407c710a787625d5f2cf365a4e3ad9232fa3f', 1, 'Huyghe', 'Mathias', NULL, 'mathias.huyghe@alumni.enac.fr', 'default_user.png', -5),
(2, 'lecarpma', '1ee3bcb7aff31f0e8d12da84deaf85b1a471731d4ed334189954e52c4b5fcdc1', 1, 'Le Carpentier', 'Marie jeanne', NULL, 'marie.le-carpentier@alumni.enac.fr', 'default_user.png', 500),
(3, 'rummenspa', '6f73aaf7bffa8141aa7c7607566063bbcf9993a1efdf79c94a9ba3ad2187595a', 1, 'Rummens', 'Paul', NULL, 'paul.rummens@alumni.enac.fr', 'default_user.png', 5700),
(4, 'vitryhu', 'ec1a405c52aee12ec05e9785d83d89b9fdc1adad1fbe38f7c7904e3e09f6686e', 1, 'Vitry', 'Hugo', NULL, 'hugo.vitry@alumni.enac.fr', 'default_user.png', 1000),
(8, 'william.johnson', 'a8d35d27edc890afc3527dbaf2fe93ac75b25c75740113ea4d2152d3a88b794f', 0, 'Johnson', 'William', 'Null', 'william.johnson@gmail.com', 'default_user.png', 0),
(9, 'olivia.johnson', 'b768ed64240186ee3849741d5dc7ea648a2797c3ea631f51861d2686a006fb58', 0, 'Johnson', 'Olivia', 'Null', 'olivia.johnson@outlook.com', 'default_user.png', 0),
(10, 'ava.wilson', 'f20c3010b1f298fd8047749600b39b48d574e818125503599fb4fbb2d16390e2', 0, 'Wilson', 'Ava', 'Null', 'ava.wilson@hotmail.com', 'default_user.png', 0),
(11, 'james.smith', 'c4b044afdf797f62d1ad6af74742a98e9e2d02f8d17bafec39c128f30ef5766a', 0, 'Smith', 'James', 'Null', 'james.smith@hotmail.com', 'default_user.png', 0),
(12, 'william.taylor', 'c4b5f3a8e950689f665759854e51462496af7d15a51f2c14b199fbdc7f2dcb22', 0, 'Taylor', 'William', 'Null', 'william.taylor@hotmail.com', 'default_user.png', 0),
(13, 'emma.johnson', '7ce99b178974ad2c9da516a85ea0e3a520e5d97cd41f5d9cdf4e233aa4b70fee', 0, 'Johnson', 'Emma', 'Null', 'emma.johnson@gmail.com', 'default_user.png', 0),
(14, 'james.wilson', 'd800599f0f231cf6901f56f508534f31480ad896751591495225a57292b9bd05', 0, 'Wilson', 'James', 'Null', 'james.wilson@outlook.com', 'default_user.png', 0),
(15, 'john.anderson', '246ad22f7331b86699affeb783cff27eb909a53411a8768b74aacdc7b954646f', 0, 'Anderson', 'John', 'Null', 'john.anderson@yahoo.com', 'default_user.png', 0),
(16, 'sophia.brown', 'a8e9b340aaffd613103fed79fd62cfc027bccd2aa76e177aef628f93ff8349e1', 0, 'Brown', 'Sophia', 'Null', 'sophia.brown@yahoo.com', 'default_user.png', 0),
(17, 'olivia.taylor', '0f9c774876349a4dac3258449793dd96ede87ba6f6ef136cbf572d76b7df0d39', 0, 'Taylor', 'Olivia', 'Null', 'olivia.taylor@hotmail.com', 'default_user.png', 0),
(18, 'isabella.taylor', 'a860ed9ce08fe0e911f66045a7d41eca03a38f81f9c72e274cdf96893abf293b', 0, 'Taylor', 'Isabella', 'Null', 'isabella.taylor@hotmail.com', 'default_user.png', 0),
(19, 'isabella.moore', '7979d0b36d07433ed0f01be761920c738c9da0953708a013c348bf108cc8e4ea', 0, 'Moore', 'Isabella', 'Null', 'isabella.moore@outlook.com', 'default_user.png', 0),
(20, 'benjamin.wilson', '67d8cad8cbe4f5176cd716d6f9765520508c24508d84dd057062006e2664cc0e', 0, 'Wilson', 'Benjamin', 'Null', 'benjamin.wilson@outlook.com', 'default_user.png', 0),
(21, 'william.taylor', 'c4b5f3a8e950689f665759854e51462496af7d15a51f2c14b199fbdc7f2dcb22', 0, 'Taylor', 'William', 'Null', 'william.taylor@gmail.com', 'default_user.png', 0),
(22, 'james.davis', '3bcc761935fba1be365d4368a01e0d095e54d875d452156f7e666751c39724ad', 0, 'Davis', 'James', 'Null', 'james.davis@hotmail.com', 'default_user.png', 0);

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
  MODIFY `idProject` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT pour la table `user`
--
ALTER TABLE `user`
  MODIFY `idUser` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

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
