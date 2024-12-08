<!-- PROJECT SHIELDS -->
<a name="readme-top"></a>
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]
[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://www.buymeacoffee.com/wanghley)

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/wanghley/recognizing-spoken-digits">
    <img src="image.gif" alt="Logo" width="280">
  </a>

  <h3 align="center">Recognizing Spoken Digits</h3>

  <p align="center">
    A project exploring Gaussian Mixture Models for spoken digit recognition using cepstral coefficients.
    <br />
    <a href="#"><strong>Explore the code »</strong></a>
    <br />
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#built-with">Built With</a></li>
    <li><a href="#getting-started">Getting Started</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

The Recognizing Spoken Digits project is part of the ECE 480 course, aimed at modeling the distributions of cepstral coefficients of spoken digits using Gaussian Mixture Models (GMMs). The project investigates two methods for estimating GMM parameters: 
1. Using k-means clustering to initialize GMM parameters.
2. Employing the Expectation-Maximization (EM) algorithm for parameter estimation.

The main goal is to explore how these modeling choices affect the performance of spoken digit recognition based on maximum likelihood classification.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="python" style="vertical-align:top; margin:4px"> <img src="https://img.shields.io/badge/Numpy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="numpy" style="vertical-align:top; margin:4px"> <img src="https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="scikit-learn" style="vertical-align:top; margin:4px"> <img src="https://img.shields.io/badge/Matplotlib-003B57?style=for-the-badge&logo=matplotlib&logoColor=white" alt="matplotlib" style="vertical-align:top; margin:4px">

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

To get started with the Recognizing Spoken Digits project, follow the instructions below:

### Prerequisites

* Python 3.x
* Numpy
* Scikit-learn
* Matplotlib

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/wanghley/recognizing-spoken-digits.git
Navigate into the project directory
