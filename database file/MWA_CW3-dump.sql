-- MySQL dump 10.13  Distrib 5.7.32, for Linux (x86_64)
--
-- Host: localhost    Database: MWA_CW3
-- ------------------------------------------------------
-- Server version	5.7.32-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `VaccineDose`
--

DROP TABLE IF EXISTS `VaccineDose`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `VaccineDose` (
  `Email` varchar(50) NOT NULL,
  `VassineGroup` varchar(5) NOT NULL,
  `VassineGroupDose` varchar(5) NOT NULL,
  PRIMARY KEY (`Email`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `VaccineDose`
--

LOCK TABLES `VaccineDose` WRITE;
/*!40000 ALTER TABLE `VaccineDose` DISABLE KEYS */;
INSERT INTO `VaccineDose` VALUES ('email.ankitapatel@gmail.com','A','0.5'),('Krutika@gmail.com','A','1.0'),('sang@gmail.com','B','0.5'),('vipul.vekaria@gmail.com','B','1.0');
/*!40000 ALTER TABLE `VaccineDose` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `VaccineMaker`
--

DROP TABLE IF EXISTS `VaccineMaker`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `VaccineMaker` (
  `Email` varchar(50) NOT NULL,
  `PasswardHash` longtext NOT NULL,
  PRIMARY KEY (`Email`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `VaccineMaker`
--

LOCK TABLES `VaccineMaker` WRITE;
/*!40000 ALTER TABLE `VaccineMaker` DISABLE KEYS */;
INSERT INTO `VaccineMaker` VALUES ('Admin','$5$rounds=535000$6MFYwMzxuqhNns/W$/4Bb8F3bieO1NQrICw3zZBvDUUj92dhTwnCrru9L5q0');
/*!40000 ALTER TABLE `VaccineMaker` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `VaccineTestResult`
--

DROP TABLE IF EXISTS `VaccineTestResult`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `VaccineTestResult` (
  `Email` varchar(50) NOT NULL,
  `TestResult` varchar(10) NOT NULL,
  PRIMARY KEY (`Email`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `VaccineTestResult`
--

LOCK TABLES `VaccineTestResult` WRITE;
/*!40000 ALTER TABLE `VaccineTestResult` DISABLE KEYS */;
INSERT INTO `VaccineTestResult` VALUES ('email.ankitapatel@gmail.com','Positive'),('Krutika@gmail.com','Negative'),('sang@gmail.com','Positive'),('vipul.vekaria@gmail.com','Positive');
/*!40000 ALTER TABLE `VaccineTestResult` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Volunteer`
--

DROP TABLE IF EXISTS `Volunteer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Volunteer` (
  `Email` varchar(50) NOT NULL,
  `PasswardHash` longtext NOT NULL,
  `Fullname` varchar(30) NOT NULL,
  `Gender` varchar(6) NOT NULL,
  `Age` int(2) NOT NULL,
  `Address` varchar(255) NOT NULL,
  `HealthInfo` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Email`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Volunteer`
--

LOCK TABLES `Volunteer` WRITE;
/*!40000 ALTER TABLE `Volunteer` DISABLE KEYS */;
INSERT INTO `Volunteer` VALUES ('email.ankitapatel@gmail.com','$5$rounds=535000$8JIvnRZrMRTbkqMg$n3WfRialOyPLjlUq9GrqGTNujCmrsVHYStVl5D/Nd03','Ankita Patel','Female',31,'71 Aylestone Road   LEICESTER LE2 7LL','N/A'),('Krutika@gmail.com','$5$rounds=535000$Sj8D.ZpnMLFG1m7Z$z8.6zxQyCja4OGyafqe6Jrxx8mxsC1LLZwgzkCmCjgD','Krutika','Female',30,'178 Clarendon Park Road   LEICESTER LE2 3AF','N/A'),('sang@gmail.com','$5$rounds=535000$QZIc9t91fg4.4DMs$gqhahrIBw6nphos.e6cagLVGoAA4qz4ay9uQfjqdhk.','Sangita patel','Female',30,'10 Moorgate Street   LEICESTER LE4 5GT','Skin Rash alergies'),('vipul.vekaria@gmail.com','$5$rounds=535000$xC3b2v10li/5Vnhb$3rigq9gA7kxeI7V5Phl6./LYUx5aF0hWXmNUjgTND79','Vipul Vekariya','Male',32,'Brew Dog 8 Friar Lane  LEICESTER LE1 5RA','N/A');
/*!40000 ALTER TABLE `Volunteer` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-01-18 19:02:06
