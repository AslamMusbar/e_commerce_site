-- phpMyAdmin SQL Dump
-- version 2.11.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Mar 06, 2024 at 02:13 PM
-- Server version: 5.0.51
-- PHP Version: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `shopme`
--

-- --------------------------------------------------------

--
-- Table structure for table `ad`
--

CREATE TABLE `ad` (
  `id` varchar(10) NOT NULL,
  `id2` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ad`
--


-- --------------------------------------------------------

--
-- Table structure for table `addcart`
--

CREATE TABLE `addcart` (
  `id` varchar(10) NOT NULL,
  `cname` varchar(100) NOT NULL,
  `ptype` varchar(100) NOT NULL,
  `pname` varchar(100) NOT NULL,
  `color` varchar(100) NOT NULL,
  `price` varchar(100) NOT NULL,
  `uname` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `addcart`
--

INSERT INTO `addcart` (`id`, `cname`, `ptype`, `pname`, `color`, `price`, `uname`, `status`) VALUES
('1', 'kr', 'notebook', 'notebook', 'red', '50', 'admin12', '2'),
('5', 'cabal', 'pain', 'calbal', 'red', '40', 'admin12', '2'),
('5', 'cabal', 'pain', 'calbal', 'red', '40', 'admin', '2'),
('7', 'test', 'test', 'test', 'red', '500', 'sam123', '2'),
('7', 'test', 'test', 'test', 'red', '500', 'sam', '2');

-- --------------------------------------------------------

--
-- Table structure for table `admintb`
--

CREATE TABLE `admintb` (
  `UserName` varchar(250) NOT NULL,
  `Password` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admintb`
--

INSERT INTO `admintb` (`UserName`, `Password`) VALUES
('admin', 'admin');

-- --------------------------------------------------------

--
-- Table structure for table `booktb`
--

CREATE TABLE `booktb` (
  `id` bigint(250) NOT NULL auto_increment,
  `Bookingid` varchar(250) NOT NULL,
  `ProductId` varchar(250) NOT NULL,
  `ProductName` varchar(250) NOT NULL,
  `UserName` varchar(250) NOT NULL,
  `Mobile` varchar(250) NOT NULL,
  `Email` varchar(250) NOT NULL,
  `Qty` varchar(250) NOT NULL,
  `Amount` varchar(250) NOT NULL,
  `Mac` varchar(250) NOT NULL,
  `CardType` varchar(250) NOT NULL,
  `CardNo` varchar(250) NOT NULL,
  `CvNo` varchar(250) NOT NULL,
  `Date` varchar(250) NOT NULL,
  `status` varchar(50) NOT NULL,
  `status1` varchar(50) NOT NULL,
  `time` varchar(50) NOT NULL,
  `dname` varchar(50) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=6 ;

--
-- Dumping data for table `booktb`
--

INSERT INTO `booktb` (`id`, `Bookingid`, `ProductId`, `ProductName`, `UserName`, `Mobile`, `Email`, `Qty`, `Amount`, `Mac`, `CardType`, `CardNo`, `CvNo`, `Date`, `status`, `status1`, `time`, `dname`) VALUES
(1, 'BOOKID001', '1', 'notebook', 'admin12', '7904461600', 'sundarv06@gmail.com', '10', '500.0', '176156945337837', 'Visacard', '1234567899', '123', '14-Mar-2023', 'packing', '1', '07:04:27', 'sundar'),
(2, 'BOOKID002', '5', 'calbal', 'admin12', '7904461600', 'sundarv06@gmail.com', '5', '200.0', '176156945337837', 'Visacard', '1234567899', '123', '23-Mar-2023', 'shipment', '1', '12:08:26', 'sundar'),
(3, 'BOOKID003', '5', 'calbal', 'admin', '7904461600', 'sundarv06@gmail.com', '1', '40.0', '176156945337837', 'Visacard', '1234567899', '1234', '02-Apr-2023', 'shipment', '1', '12:08:46', 'sundar'),
(4, 'BOOKID004', '7', 'test', 'sam123', '7904461600', 'sundarv06@gmail.com', '5', '2500.0', '176156945337837', 'Visacard', '1234567899', '123', '20-Jan-2024', 'Book', '1', '', ''),
(5, 'BOOKID005', '7', 'test', 'sam', '7904461600', 'sundarv06@gmail.com', '1', '500.0', '176156945337837', 'Visacard', '1234567899', '1234', '06-Mar-2024', 'Book', '1', '', '');

-- --------------------------------------------------------

--
-- Table structure for table `companytb`
--

CREATE TABLE `companytb` (
  `Name` varchar(250) NOT NULL,
  `Regno` varchar(250) NOT NULL,
  `Mobile` varchar(250) NOT NULL,
  `LandLine` varchar(250) NOT NULL,
  `Email` varchar(250) NOT NULL,
  `Website` varchar(250) NOT NULL,
  `Address` varchar(250) NOT NULL,
  `UserName` varchar(250) NOT NULL,
  `Password` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `companytb`
--

INSERT INTO `companytb` (`Name`, `Regno`, `Mobile`, `LandLine`, `Email`, `Website`, `Address`, `UserName`, `Password`) VALUES
('fantasy', '844101', '9600357839', '09600357839', 'fantasy@gmail.com', 'www.fantasy.com', 'no 6 trichy', 'fantasy', 'fantasy');

-- --------------------------------------------------------

--
-- Table structure for table `doctb`
--

CREATE TABLE `doctb` (
  `Name` varchar(250) NOT NULL,
  `Gender` varchar(250) NOT NULL,
  `Age` varchar(250) NOT NULL,
  `Email` varchar(250) NOT NULL,
  `Mobile` varchar(250) NOT NULL,
  `Address` varchar(250) NOT NULL,
  `UserName` varchar(250) NOT NULL,
  `Password` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `doctb`
--

INSERT INTO `doctb` (`Name`, `Gender`, `Age`, `Email`, `Mobile`, `Address`, `UserName`, `Password`) VALUES
('sundar', 'male', '24', 'anbusamcore@gmail.com', '7904461600', 'trichy', 'admin', 'test');

-- --------------------------------------------------------

--
-- Table structure for table `ownertb`
--

CREATE TABLE `ownertb` (
  `shopname` varchar(100) NOT NULL,
  `sgst` varchar(100) NOT NULL,
  `Name` varchar(250) NOT NULL,
  `Gender` varchar(250) NOT NULL,
  `Age` varchar(250) NOT NULL,
  `Email` varchar(250) NOT NULL,
  `Mobile` varchar(250) NOT NULL,
  `Address` varchar(250) NOT NULL,
  `UserName` varchar(250) NOT NULL,
  `Password` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ownertb`
--

INSERT INTO `ownertb` (`shopname`, `sgst`, `Name`, `Gender`, `Age`, `Email`, `Mobile`, `Address`, `UserName`, `Password`) VALUES
('', '', 'sundar', 'male', '24', 'sundarv06@gmail.com', '7904461600', 'trichy', 'admin', 'admin123'),
('sampletest', '12345665', 'sam', 'male', '24', 'sundarv06@gmail.com', '7904461600', 'trichy', 'admin', 'ad123'),
('sampletest', '12345665', 'sample', 'male', '30', 'test@gmail.com', '9840234119', 'trichy', 'sample', 'sample'),
('admin', '12345665', 'sam', 'male', '24', 'sundarv06@gmail.com', '7904461600', 'trichy', 'pandiyan', '1234'),
('sampletest', '12345665', 'sundar', 'male', '24', 'sundarv06@gmail.com', '7904461600', 'trichy', 'admin12', 'admin12');

-- --------------------------------------------------------

--
-- Table structure for table `protb`
--

CREATE TABLE `protb` (
  `id` bigint(250) NOT NULL auto_increment,
  `CompanyName` varchar(250) NOT NULL,
  `ProductType` varchar(250) NOT NULL,
  `ProductName` varchar(250) NOT NULL,
  `Color` varchar(250) NOT NULL,
  `Price` varchar(250) NOT NULL,
  `VideoUrl` varchar(250) NOT NULL,
  `Specifications` varchar(500) NOT NULL,
  `Image` varchar(500) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=8 ;

--
-- Dumping data for table `protb`
--

INSERT INTO `protb` (`id`, `CompanyName`, `ProductType`, `ProductName`, `Color`, `Price`, `VideoUrl`, `Specifications`, `Image`) VALUES
(1, 'kr', 'notebook', 'notebook', 'red', '50', '', ' 500page', 'imgl.gif'),
(2, 'test', 'test', 'test', '', '40', '', ' test', '123.jpeg'),
(3, 'cabal', 'pain', 'calbal', '', '1', '', ' sample', '123.jpeg'),
(4, 'cabal', 'pain', 'calbal', 'red', '40', '', ' test', '1.jpg'),
(5, 'cabal', 'pain', 'calbal', 'red', '40', '', ' test', '1.jpg'),
(6, 'test', 'test', 'test', 'red', '40', '', ' sample', 't3.jpg'),
(7, 'test', 'test', 'test', 'red', '500', '', ' test', '60786531-3d-illustration-call-center-custom-service-isolated-white-background-.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `raider`
--

CREATE TABLE `raider` (
  `Name` varchar(250) NOT NULL,
  `Gender` varchar(250) NOT NULL,
  `Age` varchar(250) NOT NULL,
  `Email` varchar(250) NOT NULL,
  `Mobile` varchar(250) NOT NULL,
  `Address` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `raider`
--

INSERT INTO `raider` (`Name`, `Gender`, `Age`, `Email`, `Mobile`, `Address`) VALUES
('sundar', 'male', '24', 'sundarv06@gmail.com', '7904461600', 'trichy');

-- --------------------------------------------------------

--
-- Table structure for table `regtb`
--

CREATE TABLE `regtb` (
  `Name` varchar(250) NOT NULL,
  `Gender` varchar(250) NOT NULL,
  `Age` varchar(250) NOT NULL,
  `Email` varchar(250) NOT NULL,
  `Mobile` varchar(250) NOT NULL,
  `Address` varchar(250) NOT NULL,
  `UserName` varchar(250) NOT NULL,
  `Password` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `regtb`
--

INSERT INTO `regtb` (`Name`, `Gender`, `Age`, `Email`, `Mobile`, `Address`, `UserName`, `Password`) VALUES
('san', 'male', '20', 'sangeeth5535@gmail.com', '9486365535', 'no 6 trichy', 'san', 'san'),
('sanNew', 'male', '20', 'sangeeth5535@gmail.com', '9486365535', 'no ', 'sanNew', 'sanNew'),
('mani', 'male', '33', 'ishu@gmail.com', '9486365535', 'dgh', 'mani', 'mani'),
('Rajiya', 'female', '20', 'rajiya@gmail.com', '948636553', 'no 6 trichy', 'rajiya', 'rajiya'),
('sundar', 'male', '29', 'sundarv06@gmail.com', '7904461600', 'trichy', 's1234', 's1234'),
('sundarapandiyan', 'male', '29', 'sundarv06@gmail.com', '7904461600', 'trichy', 'sdfg', 'sdfg'),
('sundarapandiyan', 'male', '29', 'sundarv06@gmail.com', '7904461600', 'trichy', 'admin', 'a123'),
('sundar', 'male', '24', 'sundarv06@gmail.com', '7904461600', 'trichy', 'admin', 'admin123'),
('sam', 'male', '24', 'sundarv06@gmail.com', '7904461600', 'trichy', 'admin', '12345'),
('pandiyan', 'male', '24', 'sundarv06@gmail.com', '7904461600', 'trichy', 'admin', 'admin123'),
('sample', 'male', '23', 'sundarv06@gmail.com', '7904461600', 'trichy', 'admin', '123456'),
('sundar', 'male', '24', 'anbusamcore@gmail.com', '7904461600', 'trichy', 'admin', 'test'),
('sample', 'male', '24', 'sundarv06@gmail.com', '7904461600', 'trichy', 'admin', 'admin123'),
('admin', 'male', '24', 'sundarv06@gmail.com', '7904461600', 'trichy', 'admin12', 'ad12'),
('sample', 'male', '23', 'test@gmail.com', '9840234119', 'trichy', 'admin', '123456'),
('sample', 'male', '30', 'sundarv06@gmail.com', '7904461600', 'trichy', 'sam123', 'sam123'),
('sundar', 'male', '30', 'sundarv06@gmail.com', '7904461600', 'trichy', 'sam', 'sam');

-- --------------------------------------------------------

--
-- Table structure for table `reviewtb`
--

CREATE TABLE `reviewtb` (
  `id` bigint(250) NOT NULL auto_increment,
  `ProductId` varchar(250) NOT NULL,
  `CompanyName` varchar(250) NOT NULL,
  `ProductType` varchar(250) NOT NULL,
  `ProductName` varchar(250) NOT NULL,
  `Price` varchar(250) NOT NULL,
  `Image` varchar(500) NOT NULL,
  `Bookid` varchar(250) NOT NULL,
  `Email` varchar(250) NOT NULL,
  `MacAddress` varchar(250) NOT NULL,
  `UserName` varchar(250) NOT NULL,
  `Rate` int(250) NOT NULL,
  `Review` varchar(500) NOT NULL,
  `Smile1` int(250) NOT NULL,
  `Smile2` int(250) NOT NULL,
  `Smile3` int(250) NOT NULL,
  `Smile4` int(250) NOT NULL,
  `Smile5` int(250) NOT NULL,
  `Smile6` int(250) NOT NULL,
  `Result` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=9 ;

--
-- Dumping data for table `reviewtb`
--

INSERT INTO `reviewtb` (`id`, `ProductId`, `CompanyName`, `ProductType`, `ProductName`, `Price`, `Image`, `Bookid`, `Email`, `MacAddress`, `UserName`, `Rate`, `Review`, `Smile1`, `Smile2`, `Smile3`, `Smile4`, `Smile5`, `Smile6`, `Result`) VALUES
(2, '', 'kr', 'notebook', 'notebook', '50', 'imgl.gif', '', '', '', '', 5, 'good', 0, 0, 0, 0, 0, 0, 'Nagative'),
(3, '', 'kr', 'notebook', 'notebook', '50', 'imgl.gif', '', '', '', '', 5, 'good', 0, 0, 0, 0, 0, 0, 'Postive'),
(4, '1', 'kr', 'notebook', 'notebook', '50', 'imgl.gif', '', '', '', '', 5, 'good', 0, 0, 0, 0, 0, 0, 'Postive'),
(5, '2', 'test', 'test', 'test', '40', '123.jpeg', '', '', '', '', 1, 'what interview! leave me alone,leave me alone', 0, 0, 0, 0, 0, 0, 'Nagative'),
(6, '2', 'test', 'test', 'test', '40', '123.jpeg', '', '', '', '', 4, 'I will say this about the patch. It work for me. We&#039;re there side effects? yes. A small bit of bruising and a small rash.I ', 0, 0, 0, 0, 0, 0, 'Postive'),
(7, '2', 'test', 'test', 'test', '40', '123.jpeg', '', '', '', '', 4, 'BC from below. Rapid weight gain, swelling and bad cycle. Dont recommend', 0, 0, 0, 0, 0, 0, 'Nagative'),
(8, '2', 'test', 'test', 'test', '40', '123.jpeg', '', '', '', '', 5, 'good', 0, 0, 0, 0, 0, 0, 'Postive');

-- --------------------------------------------------------

--
-- Table structure for table `temptb`
--

CREATE TABLE `temptb` (
  `ProductId` varchar(250) NOT NULL,
  `CompanyName` varchar(250) NOT NULL,
  `ProductType` varchar(250) NOT NULL,
  `ProductName` varchar(250) NOT NULL,
  `Price` varchar(250) NOT NULL,
  `Image` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `temptb`
--

INSERT INTO `temptb` (`ProductId`, `CompanyName`, `ProductType`, `ProductName`, `Price`, `Image`) VALUES
('4', 'Samsung', 'TV', 'SamsungTv', '800', 'images_1.jpg'),
('6', 'Apple', 'Watch', 'Applewatch', '8000', 'download.jpg'),
('5', 'Apple', 'TV', 'Apple Tv', '9000', 'Penguins.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `userques`
--

CREATE TABLE `userques` (
  `id` int(50) NOT NULL auto_increment,
  `name` varchar(100) NOT NULL,
  `dname` varchar(100) NOT NULL,
  `details` varchar(100) NOT NULL,
  `ans` varchar(100) NOT NULL,
  `status` varchar(10) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `userques`
--

INSERT INTO `userques` (`id`, `name`, `dname`, `details`, `ans`, `status`) VALUES
(1, 'admin', 'colpal', 'sampler', 'sample', '1'),
(2, 'admin', 'colpal', 'pain killer', 'ok good', '1');
