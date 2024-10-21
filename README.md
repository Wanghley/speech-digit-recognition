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
   ```
2. Navigate into the project directory
   ```sh
   cd recognizing-spoken-digits
   ```
3. Install the required packages
   ```sh
   pip install -r requirements.txt
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE -->
## Usage

This project provides a framework for recognizing spoken digits using cepstral coefficients. The main functionalities include training GMMs with the training dataset and evaluating recognition performance with the testing dataset.

### How to Run

To execute the project, use the following command in your terminal:

```bash
python main.py <train_file> <test_file>
```

Example:

```bash
python main.py Train_Arabic_Digit.txt Test_Arabic_Digit.txt
```

### Input Format

- `<train_file>`: The name of the training dataset file (e.g., `Train_Arabic_Digit.txt`).
- `<test_file>`: The name of the testing dataset file (e.g., `Test_Arabic_Digit.txt`).

### Features

1. **Modeling Approaches**:
   - GMM parameter initialization using k-means clustering.
   - Parameter estimation using the EM algorithm.
   
2. **Classification**:
   - Maximum likelihood classification of spoken digits.

3. **Cepstral Coefficient Selection**:
   - Investigate the impact of using all or a subset of cepstral coefficients.

4. **Covariance Constraints**:
   - Explore different constraints on the GMM covariance matrices (diagonal, tied, spherical).

5. **Data Aggregation**:
   - Assess the impact of different frame aggregation methods on model performance.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap
- [ ] Implement data loading and preprocessing
- [ ] Display the distribution of cepstral coefficients
- [ ] Implement GMM training with k-means initialization
- [ ] Implement GMM training using the EM algorithm
- [ ] Conduct performance evaluation of the two approaches
- [ ] Explore cepstral coefficient selection strategies
- [ ] Investigate covariance matrix constraints
- [ ] Analyze the impact of frame aggregation methods

See the [open issues](https://github.com/wanghley/recognizing-spoken-digits/issues) for a full list of proposed features and known issues.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are welcome! If you have suggestions, improvements, or bug fixes, feel free to open an issue or submit a pull request.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Wanghley - [your.email@example.com](mailto:your.email@example.com)  
Project Link: [https://github.com/wanghley/recognizing-spoken-digits](https://github.com/wanghley/recognizing-spoken-digits)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

- [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Spoken+Arabic+Digit)
- Special thanks to Professor [Name] for guidance and support.

<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/wanghley/Digit-Recognition-from-Speech?style=for-the-badge
[contributors-url]: https://github.com/wanghley/Digit-Recognition-from-Speech/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/wanghley/Digit-Recognition-from-Speech.svg?style=for-the-badge
[forks-url]: https://github.com/wanghley/Digit-Recognition-from-Speech/network/members
[stars-shield]: https://img.shields.io/github/stars/wanghley/Digit-Recognition-from-Speech.svg?style=for-the-badge
[stars-url]: https://github.com/wanghley/Digit-Recognition-from-Speech/stargazers
[issues-shield]: https://img.shields.io/github/issues/wanghley/Digit-Recognition-from-Speech.svg?style=for-the-badge
[issues-url]: https://github.com/wanghley/Digit-Recognition-from-Speech/issues
[license-shield]: https://img.shields.io/github/license/wanghley/Digit-Recognition-from-Speech.svg?style=for-the-badge
[license-url]: https://github.com/wanghley/Digit-Recognition-from-Speech/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/wanghley
[product-screenshot]: images/screenshot.png