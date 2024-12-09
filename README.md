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
  <a href="https://github.com/Wanghley/speech-digit-recognition">
    <img src="image.gif" alt="Logo" width="280">
  </a>

  <h3 align="center">Recognizing Spoken Digits</h3>

  <p align="center">
    A project exploring Gaussian Mixture Models for spoken digit recognition using cepstral coefficients.
    <br />
    <a href="https://github.com/Wanghley/speech-digit-recognition"><strong>Explore the code »</strong></a>
    <br />
  </p>
</div>

---

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

---

<!-- ABOUT THE PROJECT -->
## About The Project

The **Recognizing Spoken Digits** project is part of the ECE 480 course, focusing on using Gaussian Mixture Models (GMMs) to recognize spoken digits. This project models the distributions of cepstral coefficients, which are widely used in speech processing and recognition. 

Key objectives:
1. **Parameter Initialization**: Use k-means clustering to initialize GMM parameters.
2. **Parameter Estimation**: Apply the Expectation-Maximization (EM) algorithm to refine these parameters.

The primary goal is to evaluate how these modeling techniques impact spoken digit recognition using a **maximum likelihood classification** approach.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

<!-- BUILT WITH -->
### Built With

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) 
![Numpy](https://img.shields.io/badge/Numpy-013243?style=for-the-badge&logo=numpy&logoColor=white) 
![Scikit-learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white) 
![Matplotlib](https://img.shields.io/badge/Matplotlib-003B57?style=for-the-badge&logo=matplotlib&logoColor=white)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

<!-- GETTING STARTED -->
## Getting Started

Follow the steps below to set up and run the project locally.

### Prerequisites

Make sure you have the following installed:
- Python 3.x
- Numpy
- Scikit-learn
- Matplotlib

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/wanghley/recognizing-spoken-digits.git
   ```
2. Navigate to the project directory:
   ```sh
   cd recognizing-spoken-digits
   ```
3. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

<!-- USAGE -->
## Usage

Run the project to test the performance of Gaussian Mixture Models on spoken digit recognition. You can modify the parameters of the k-means and EM algorithms to observe the impact on classification accuracy.

1. Train the GMM model:
   ```sh
   python train.py
   ```
2. Evaluate the model:
   ```sh
   python evaluate.py
   ```

For more details, refer to the project files or documentation.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

<!-- ROADMAP -->
## Roadmap

- [ ] Add support for additional datasets.
- [ ] Explore other feature extraction techniques.
- [ ] Improve model accuracy through hyperparameter tuning.
- [ ] Create a user-friendly interface for testing the model.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

<!-- CONTRIBUTING -->
## Contributing

Contributions are welcome! If you have ideas or improvements, please fork the repository and submit a pull request. 

1. Fork the project.
2. Create your feature branch:
   ```sh
   git checkout -b feature/AmazingFeature
   ```
3. Commit your changes:
   ```sh
   git commit -m 'Add some AmazingFeature'
   ```
4. Push to the branch:
   ```sh
   git push origin feature/AmazingFeature
   ```
5. Open a pull request.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

<!-- CONTACT -->
## Contact

Wanghley - [LinkedIn](https://linkedin.com/in/wanghley) - wanghley@example.com

Project Link: [https://github.com/wanghley/recognizing-spoken-digits](https://github.com/wanghley/recognizing-spoken-digits)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

- [Scikit-learn Documentation](https://scikit-learn.org/stable/documentation.html)
- [Python Official Documentation](https://docs.python.org/3/)
- [Matplotlib Documentation](https://matplotlib.org/stable/users/index.html)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
```

### Improvements:
1. **Clearer Structure**: Organized content into sections with consistent formatting.
2. **Enhanced Language**: Improved readability and professionalism.
3. **Interactive Links**: Added direct links to the repository and other references.
4. **Actionable Instructions**: Added detailed steps for setup, usage, and contributing.
5. **Visual Elements**: Used badges for a polished look.


<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/wanghley/speech-digit-recognition?style=for-the-badge
[contributors-url]: https://github.com/wanghley/speech-digit-recognition/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/wanghley/speech-digit-recognition.svg?style=for-the-badge
[forks-url]: https://github.com/wanghley/speech-digit-recognition/network/members
[stars-shield]: https://img.shields.io/github/stars/wanghley/speech-digit-recognition.svg?style=for-the-badge
[stars-url]: https://github.com/wanghley/speech-digit-recognition/stargazers
[issues-shield]: https://img.shields.io/github/issues/wanghley/speech-digit-recognition.svg?style=for-the-badge
[issues-url]: https://github.com/wanghley/speech-digit-recognition/issues
[license-shield]: https://img.shields.io/github/license/wanghley/speech-digit-recognition.svg?style=for-the-badge
[license-url]: https://github.com/wanghley/speech-digit-recognition/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/wanghley