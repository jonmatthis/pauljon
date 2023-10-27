+++++++++++++++++++++++++++++++++++

Explanation: This document can be categorized as an "Explanation" type of documentation in the Diataxis framework. It provides troubleshooting information and aims to help users gain a deeper understanding of specific problems and how to fix them. It focuses on providing context and illuminating concepts related to troubleshooting.

-----------------------------------

+++++++++++++++++++++++++++++++++++

**Explanation: Understanding-oriented discussion to provide context and illuminate concepts. Help users gain deeper knowledge.**

The document titled "About Us" provides an explanation of the Free Motion Capture Project (FreeMoCap). It explains the project's goal of providing research-grade markerless motion capture software for free. The document also highlights the project's focus on creating a user-friendly framework that connects various open-source tools from the computer vision and machine learning communities. It emphasizes the aim of making these technologies accessible to a wide range of communities. The document discusses the project's development philosophy of "Universal Design" and its potential benefits for different user groups. It also includes a video and provides an overview of the software's features and capabilities. Additionally, it mentions the community involvement and support available through a Discord server and GitHub. Overall, this document provides a deeper understanding of the project's objectives, technologies, and community engagement.

-----------------------------------

+++++++++++++++++++++++++++++++++++

# Tutorials: Getting Started with FreeMoCap

This document serves as a tutorial-oriented guide to help users learn the basic skills needed to get started with FreeMoCap. It provides a quick start guide and directs users to the Single-Camera Recording walkthrough in the Tutorials section. The goal of this document is to help users get started using FreeMoCap.

## Helpful Links

- The FreeMoCap Website [https://freemocap.org](https://freemocap.org)
- The FreeMoCap GitHub [https://github.com/freemocap/freemocap](https://github.com/freemocap/freemocap)
- Support FreeMoCap by [donating to our non-profit](https://freemocap.org/about-us.html#donate) that supports our work!

## Troubleshooting?

- If you run into an issue using the software itself, post an issue on our GitHub, here: [https://github.com/freemocap/freemocap/issues](https://github.com/freemocap/freemocap/issues)   
- If there's an error in our documentation, post an issue on our documentation repository, here: [https://github.com/freemocap/documentation/issues](https://github.com/freemocap/documentation/issues)
- Join the Discord and ask a question in the #help-requests channel.
    - [Click here to join our Discord](https://discord.gg/P2nyraRYjb)

-----------------------------------

+++++++++++++++++++++++++++++++++++

# Explanation: Terminology

This document provides a brief explanation of the terminology used in the project. It includes definitions for "Capture Volume," "Calibration," "Charuco Board," "Mediapipe," and "Processing Stages." The document serves as a reference for users to find factual information about the project's terminology.

# Explanation: Capture Volume

This document explains the concept of a capture volume in the context of the project. It describes a capture volume as a 3-dimensional area with sufficient camera coverage to support 3D tracking. The document serves as an explanation to help users gain a deeper understanding of the project.

# Explanation: Calibration

This document provides information about calibration in the project. It includes a link to a section of a video discussing capture volume calibration. The document serves as an explanation to help users understand the calibration process in the project.

# Explanation: Charuco Board

This document provides information about the charuco board used in the project. It includes a link to a section of a video discussing capture volume calibration. The document serves as an explanation to help users understand the role of the charuco board in the calibration process.

# Reference: Mediapipe

This document provides a reference to the Mediapipe solution used in the project. It includes a link to the official Mediapipe documentation. The document serves as a reference for users to find factual information about using Mediapipe in the project.

# Explanation: Processing Stages

This document describes the different processing stages necessary to use USB webcams for 3D kinematic data reconstruction. It provides an overview of each stage, including recording videos, synchronizing videos, calibrating the capture volume, tracking 2D points, reconstructing 3D, using Blender for output data files, and saving skeleton animation. The document serves as an explanation to help users understand the overall process and workflow of the project.

# Explanation: Reprojection Error

This document explains the concept of reprojection error in the project. It defines reprojection error as the distance between the originally measured 2D point and the reconstructed 3D point reprojected back onto the image plane. The document provides insights into the factors that can contribute to reprojection error and includes a link to a conversation about reprojection error on Discord. It serves as an explanation to help users understand the concept and its implications in the project.

-----------------------------------

+++++++++++++++++++++++++++++++++++

**Document Type: How-To Guide**

**Summary:**
This document serves as a guide for users who want to propose new ideas and feature requests for the project. It provides instructions on how to open a new issue on GitHub and includes a list of details that should be included in the feature request. The document also emphasizes that not all requested features can be implemented, but each request will be considered and prioritized based on the project and community needs.

-----------------------------------

+++++++++++++++++++++++++++++++++++

DOCUMENT TYPE: Explanation

SUMMARY: 
This document provides guidelines for maintaining code readability, quality, and maintainability. It covers general guidelines such as following a Universal Design approach and adhering to PEP 8 Guidelines. It also includes specific guidelines for using Google-formatted docstrings, type hints, keyword arguments, private methods and attributes, descriptive names, PEP8 and `black` formatting, consistent naming conventions, keeping functions and methods short, modularizing code, minimizing comments, error handling, writing tests, and performing code reviews. This document serves as an understanding-oriented discussion to provide context and illuminate concepts related to maintaining code quality and best practices.

-----------------------------------

+++++++++++++++++++++++++++++++++++

### How-To Guide: Writing Detailed Bug Reports

This document provides guidance on how to write detailed bug reports for the project. Bug reports are essential for identifying and resolving issues in the software. By following the guidelines outlined in this document, users can effectively communicate their problems to the community and maintainers, increasing the likelihood of receiving assistance.

Key elements of a great bug report include:

- A quick summary and/or background of the issue.
- Detailed steps to reproduce the bug, including specific instructions and any necessary files or code.
- Providing sample code or relevant resources that demonstrate the problem.
- Clearly stating the expected behavior and what actually happens.
- Including any additional notes, such as possible causes or attempted solutions.

Thorough bug reports greatly assist the community and maintainers in understanding and addressing the reported issues. By following the guidelines in this document, users can contribute to the improvement of the project by effectively communicating their problems.

-----------------------------------

+++++++++++++++++++++++++++++++++++

# Explanation: Contributing to the FreeMoCap Project

This document provides guidance on how to contribute to the FreeMoCap project. It covers various aspects such as reporting bugs, suggesting new features, and submitting code changes. The document aims to onboard contributors and facilitate collaboration.

## Getting Started

This section provides an overview of how to get started with the FreeMoCap project.

## Installing FreeMoCap from source code

This section explains the process of installing FreeMoCap from its source code.

## Reporting Bugs

In this section, users learn how to report bugs and suggest new features for the project. It directs them to the Bug Report guide for detailed instructions.

## Suggesting Features

This section encourages users to suggest new features or improvements to FreeMoCap. It provides a link to open a new issue and outlines the information to include when suggesting a feature.

## Code Contributions

This section focuses on contributing code to FreeMoCap. It introduces the development process, coding styles, and testing requirements.

### We Use GitHub Flow

This subsection explains that the project follows the GitHub Flow development process, making it easy for contributors to submit changes and for maintainers to review and merge them.

### Code Changes Happen Through Pull Requests

This subsection emphasizes the use of pull requests for proposing code changes. It provides a step-by-step guide on creating a pull request.

### Coding Styles

This subsection highlights the importance of consistent coding styles and provides links to the style guides used in the project.

### Testing

This subsection emphasizes the requirement for tests in code contributions. It advises contributors to ensure their code is covered by tests and passes the project's testing workflow.

### Pull Requests

This subsection reiterates the use of pull requests for proposing code changes and provides a step-by-step guide on creating a pull request.

## Getting Help and Asking Questions

This section informs users about the available support channels, such as the Discord server and GitHub issue tracker, where they can seek assistance and ask questions.

-----------------------------------

+++++++++++++++++++++++++++++++++++

DOCUMENT SUMMARY:

This document is a Code of Conduct for the project's community. It sets the standards for behavior and aims to create an open and welcoming environment for all participants. It emphasizes the importance of using inclusive language, respecting differing viewpoints, accepting constructive criticism, and focusing on the best interests of the community. It also outlines examples of unacceptable behavior, such as harassment and the use of inappropriate language or imagery. The document encourages conflict resolution through respectful dialogue and offers contact information for assistance if needed. 

This document falls under the "Reference" type of documentation as it provides information-oriented technical descriptions of the project's community standards. It helps users find factual information about the expected behavior and conduct within the community.

-----------------------------------

+++++++++++++++++++++++++++++++++++

# Explanation: Privacy Policy

The Privacy Policy document provides an understanding-oriented discussion to provide context and illuminate concepts related to the collection, use, and protection of user data. It falls under the Explanation type of documentation in the Diataxis framework.

The document explains that the FreeMoCap development team respects and values user privacy. It outlines how personal or anonymous data is collected, used, and protected when users interact with the software. The document also highlights the option for users to control their data by enabling or disabling the collection of anonymous usage information.

In terms of the Diataxis Documentation framework, this document falls under the Explanation type as it aims to help users gain a deeper knowledge and understanding of the privacy practices implemented by the FreeMoCap software. It provides context and illuminates concepts related to user data collection, protection, and control.

Overall, the Privacy Policy document serves the user need for understanding and transparency regarding the handling of their data.

-----------------------------------

+++++++++++++++++++++++++++++++++++

DOCUMENT TYPE: Tutorials

SUMMARY: 
This document provides the necessary equipment and software prerequisites for using FreeMoCap, an open-source software for motion capture. It outlines the required equipment, such as cameras and a Charuco board for calibration, as well as the necessary software, including Blender and optional tools like VS Code or JupyterLab. The document also mentions the recommended installation method using a virtual environment management software like Anaconda.

-----------------------------------

+++++++++++++++++++++++++++++++++++

**Document Type: How-To Guide**

**Summary:**
This document provides guidance on setting up the environment for FreeMoCap, a camera-based system. It emphasizes the importance of lighting conditions and suggests using bright environments for optimal results. It explains the concept of exposure time and how it affects motion blur and the identification of subject joints. The document also discusses background considerations, such as using a solid-colored backdrop and subjects wearing tight-fitting clothes. Additionally, it provides recommendations for camera placement and configuration in multi-camera setups, including capturing a standing human in a tighter space and separating cameras to improve triangulation. The document highlights the need for good lighting, optimal camera settings, and successful calibration for high-quality recordings.

-----------------------------------

+++++++++++++++++++++++++++++++++++

## Tutorials - Single-Camera Recording

### Introduction
The Single-Camera Recording tutorial is designed to help users get started with the FreeMoCap software by creating a single-camera recording and reconstruction of their movement. This tutorial is recommended for all users, especially those who are new to the software.

### Installation
Before starting the tutorial, users are advised to follow the Installation Guide to install the FreeMoCap software. This step is essential to ensure that the software works properly on the user's computer with their hardware.

### Launching FreeMoCap
Once the software is installed, users can launch FreeMoCap from the terminal by activating the relevant Python environment and typing `freemocap` into the terminal. This will open the GUI, which is the main interface for the software.

### Camera Detection
After launching FreeMoCap, the software will automatically detect the connected cameras and display a viewpoint from the camera in the GUI. Users can adjust the camera settings, such as exposure, to optimize the image quality. It is recommended to keep the exposure setting as low as possible to decrease blur.

### Recording
To start the recording, users can click the "Start a New Recording" button in the GUI and then click the "Detect Cameras" button. This will initiate the recording process. Users can perform movements within the camera's field of view and then click the "Stop" button to end the recording. The software will automatically process the recording and generate output files.

By following this tutorial, users will gain a baseline understanding of the recording process and ensure that the software is functioning correctly on their computer. This tutorial serves as a starting point for users before moving on to more complex tasks like multi-camera calibration and reconstruction.

-----------------------------------

+++++++++++++++++++++++++++++++++++

This document can be classified as a tutorial in the Diataxis Documentation framework. It provides a step-by-step guide for users to get started with the software. The document starts with installation instructions and then walks users through the process of creating a new recording, recording videos, calibrating the capture volume, performing 3D reconstruction, post-processing, and visualization. This tutorial is aimed at helping users learn the basic skills required to use the software effectively.

-----------------------------------

+++++++++++++++++++++++++++++++++++

## How-To Guide: Multi-Camera Calibration

This guide provides step-by-step instructions on how to perform multi-camera calibration using the anipose-based calibration method. Please note that we will soon be updating our method to use a more flexible and interactive interface.

### Preparing the Charuco Board
To start the calibration process, you'll need to print out a Charuco board image. For smaller spaces, a standard printer should suffice. However, for larger spaces, consider printing the board on a poster board for better visibility from the cameras.

### Recording Calibration Videos
In the GUI's camera view section, select the calibration videos option. Begin recording and move the Charuco board until it is visible in the overlapping fields of view of at least two cameras simultaneously. Ensure that each camera captures shared views of the board with at least one other camera. These shared views will help determine the relative positions of the cameras for the 3D triangulation step later.

For more detailed instructions on using the board for high-quality calibration, refer to this video (note that it uses a different version of the software, but the principles remain the same).

### Processing the Calibration
Once each camera has captured sufficient views of the board, click "Stop Recording" to initiate the automatic calibration process. Keep an eye on the terminal that launched the GUI for helpful output, as the log at the bottom of the GUI screen may not capture all the necessary information.

This how-to guide provides clear instructions for users to accomplish the specific goal of multi-camera calibration. By following these steps, users can accurately calibrate their cameras for optimal performance.

-----------------------------------

+++++++++++++++++++++++++++++++++++

# TUTORIAL: Installation

This document provides a step-by-step guide to help users get started with the installation of the software. It falls under the "Tutorials" category of the Diataxis Documentation framework. The goal of this document is to teach users the basic skills required to install the software.

The document begins with a quickstart section that provides a concise command to install the software. It then proceeds to explain the installation process in detail, including instructions for opening a terminal window and creating a new Python environment. The document also provides options for installing the software from PyPi or GitHub.

Once the installation is complete, users are instructed to launch the GUI. The document concludes by directing users to the next steps, which can be found in the Single-Camera Tutorial or Multi-Camera Calibration Guide sections.

Overall, this document serves the user need of learning how to install the software and get started with it. It fits into the Diataxis Documentation framework as a tutorial that helps users acquire the necessary skills for using the product.

-----------------------------------

=============================================================

=============================================================

___ 
 > Global Summary 
  Here is a summary of the current state of the FreeMoCap documentation and suggestions for improvement based on the Diataxis framework:

# Current State of Documentation

## What exists:
- Getting Started
  - Installation guide
  - Single camera recording tutorial
  - Multi-camera calibration guide
- Troubleshooting guide
- About Us page
- Terminology reference

## Gaps/Missing pieces:
- No overview explaining the software and its purpose 
- No conceptual explanations of how the software works
- No task-focused how-to guides beyond the getting started tutorial
- No detailed reference documentation on code APIs or parameters

# Suggested Improvements

## Add Overview/Explanation Docs
- Add a software overview page explaining FreeMoCap at a high level
- Add conceptual explainers covering core techniques like calibration, 2D tracking, 3D reconstruction etc. 

## Expand How-To Guides
- Add how-to guides for common tasks like:
  - Recording with multiple asynchronous cameras
  - Using alternative tracking algorithms
  - Customizing and exporting data
  - Integrating with animation software

## Create Detailed Reference Docs 
- Document code APIs and parameters for

```

🌱
├── troubleshooting.md
│   ├── type: file
│   └── content
│       ├── file_name: troubleshooting.md
│       ├── file_type: .md
│       ├── file_stats
│       │   ├── bytes: 76
│       │   ├── last_modified_utc: 1698362088.4299002
│       │   ├── last_accessed_utc: 1698362090.245869
│       │   └── created_utc: 1698362088.4299002
│       └── content: Troubleshooting
│            For fixing specific problems
│           
│           # Installation problems
│           # Etc
├── about_us.md
│   ├── type: file
│   └── content
│       ├── file_name: about_us.md
│       ├── file_type: .md
│       ├── file_stats
│       │   ├── bytes: 3257
│       │   ├── last_modified_utc: 1698362088.4138987
│       │   ├── last_accessed_utc: 1698362088.6010447
│       │   └── created_utc: 1698362088.4138987
│       └── content: 
│           **The Free Motion Capture Project (FreeMoCap) aims to provide 
│           research-grade markerless motion capt
│           ...
│           f the community. Feature requests and bug reports should be 
│           submitted to the GitHub issues space.
│           
│           
│           
├── index.md
│   ├── type: file
│   └── content
│       ├── file_name: index.md
│       ├── file_type: .md
│       ├── file_stats
│       │   ├── bytes: 1371
│       │   ├── last_modified_utc: 1698362088.4290123
│       │   ├── last_accessed_utc: 1698362089.6185477
│       │   └── created_utc: 1698362088.4290123
│       └── content: # Welcome Skele-Friend! 💀✨
│           
│           This is the official and most up-to-date place to find documentation
│           for
│           ...
│            the #help-requests channel.
│               - [Click here to join our 
│           Discord](https://discord.gg/P2nyraRYjb)
│           
│           
├── terminology/
│   └── terminology.md
│       ├── type: file
│       └── content
│           ├── file_name: terminology.md
│           ├── file_type: .md
│           ├── file_stats
│           │   ├── bytes: 4230
│           │   ├── last_modified_utc: 1698362088.4296792
│           │   ├── last_accessed_utc: 1698362089.626333
│           │   └── created_utc: 1698362088.4296792
│           └── content: # Terminology
│               
│               ## Capture Volume
│               3-dimensional area (volume) with sufficient camera coverage to 
│               supp
│               ...
│                on 
│               discord](https://discord.com/channels/760487252379041812/7604896
│               02917466133/989189718203838505)
│               
├── contributing/
│   ├── feature_request.md
│   │   ├── type: file
│   │   └── content
│   │       ├── file_name: feature_request.md
│   │       ├── file_type: .md
│   │       ├── file_stats
│   │       │   ├── bytes: 683
│   │       │   ├── last_modified_utc: 1698362088.4275131
│   │       │   ├── last_accessed_utc: 1698362088.6179833
│   │       │   └── created_utc: 1698362088.4275131
│   │       └── content: We welcome new ideas and feature requests from the 
│   │           community! To propose a new feature or enhancemen
│   │           ...
│   │           ill consider each request and prioritize them based on the needs
│   │           of the project and the community.
│   │           
│   │           
│   ├── python_code_style_guide.md
│   │   ├── type: file
│   │   └── content
│   │       ├── file_name: python_code_style_guide.md
│   │       ├── file_type: .md
│   │       ├── file_stats
│   │       │   ├── bytes: 2762
│   │       │   ├── last_modified_utc: 1698362088.427817
│   │       │   ├── last_accessed_utc: 1698362088.62457
│   │       │   └── created_utc: 1698362088.427817
│   │       └── content: 
│   │             
│   │           This style guide aims to maintain code readability, quality, and
│   │           maintainability. 
│   │             
│   │           ## General
│   │           ...
│   │           Code reviews**: Perform code reviews with team members or peers 
│   │           to maintain a high-quality codebase.
│   ├── bug_report.md
│   │   ├── type: file
│   │   └── content
│   │       ├── file_name: bug_report.md
│   │       ├── file_type: .md
│   │       ├── file_stats
│   │       │   ├── bytes: 866
│   │       │   ├── last_modified_utc: 1698362088.4273918
│   │       │   ├── last_accessed_utc: 1698362089.1185822
│   │       │   └── created_utc: 1698362088.4273918
│   │       └── content: 
│   │           ### Write bug reports with detail, background, and sample code
│   │           
│   │           [This is an example](http://stackov
│   │           ...
│   │           maintainers will help you with your issues stems from how well 
│   │           you can help them understand you. :)
│   │           
│   └── index.md
│       ├── type: file
│       └── content
│           ├── file_name: index.md
│           ├── file_type: .md
│           ├── file_stats
│           │   ├── bytes: 3204
│           │   ├── last_modified_utc: 1698362088.4276304
│           │   ├── last_accessed_utc: 1698362088.600225
│           │   └── created_utc: 1698362088.4276304
│           └── content: # Contributing to the FreeMoCap Project
│               
│               
│               Welcome to the FreeMoCap contributing guide! 
│               
│               This docume
│               ...
│               ating a new issue on Github. We'll do our best to assist you and
│               provide the information you need.
│               
│               
├── community/
│   ├── code_of_conduct.md
│   │   ├── type: file
│   │   └── content
│   │       ├── file_name: code_of_conduct.md
│   │       ├── file_type: .md
│   │       ├── file_stats
│   │       │   ├── bytes: 1515
│   │       │   ├── last_modified_utc: 1698362088.42693
│   │       │   ├── last_accessed_utc: 1698362088.5958352
│   │       │   └── created_utc: 1698362088.42693
│   │       └── content: # Code of Conduct
│   │           
│   │           
│   │           In the interest of fostering an open and welcoming environment, 
│   │           we as contributo
│   │           ...
│   │           cap dot org and we will do our best to facilitate resolution by 
│   │           providing guidance and mediation.
│   │           
│   │           
│   │           
│   └── privacy_policy.md
│       ├── type: file
│       └── content
│           ├── file_name: privacy_policy.md
│           ├── file_type: .md
│           ├── file_stats
│           │   ├── bytes: 2837
│           │   ├── last_modified_utc: 1698362088.4272044
│           │   ├── last_accessed_utc: 1698362088.5998137
│           │   └── created_utc: 1698362088.4272044
│           └── content: # Privacy Policy
│               
│               We respect and value your privacy. This Privacy Policy outlines 
│               how we collect, us
│               ...
│               se of your data, please contact us at info AT freemocap DOT org,
│               or reach out to us on our Discord.
│               
├── assets/
│   ├── fmc-logo-transparent-bkgd.png
│   │   ├── type: file
│   │   └── content
│   │       ├── file_name: fmc-logo-transparent-bkgd.png
│   │       ├── file_type: .png
│   │       ├── file_stats
│   │       │   ├── bytes: 312185
│   │       │   ├── last_modified_utc: 1698362088.4154236
│   │       │   ├── last_accessed_utc: 1698362948.5618947
│   │       │   └── created_utc: 1698362088.4154236
│   │       └── content: <content could not be loaded>
│   ├── skelly_freemocap_favicon.ico
│   │   ├── type: file
│   │   └── content
│   │       ├── file_name: skelly_freemocap_favicon.ico
│   │       ├── file_type: .ico
│   │       ├── file_stats
│   │       │   ├── bytes: 43024
│   │       │   ├── last_modified_utc: 1698362088.4259763
│   │       │   ├── last_accessed_utc: 1698362948.565643
│   │       │   └── created_utc: 1698362088.4259763
│   │       └── content: <content could not be loaded>
│   ├── skelly_freemocap_logo.png
│   │   ├── type: file
│   │   └── content
│   │       ├── file_name: skelly_freemocap_logo.png
│   │       ├── file_type: .png
│   │       ├── file_stats
│   │       │   ├── bytes: 124710
│   │       │   ├── last_modified_utc: 1698362088.426702
│   │       │   ├── last_accessed_utc: 1698362948.5657327
│   │       │   └── created_utc: 1698362088.426702
│   │       └── content: <content could not be loaded>
│   ├── images/
│   │   └── freemocap_calibration_window_w_text_overlay.png
│   │       ├── type: file
│   │       └── content
│   │           ├── file_name: freemocap_calibration_window_w_text_overlay.png
│   │           ├── file_type: .png
│   │           ├── file_stats
│   │           │   ├── bytes: 2172925
│   │           │   ├── last_modified_utc: 1698362088.4254177
│   │           │   ├── last_accessed_utc: 1698362948.5625072
│   │           │   └── created_utc: 1698362088.4254177
│   │           └── content: <content could not be loaded>
│   └── icons/
│       ├── skull-sparkle.svg
│       │   ├── type: file
│       │   └── content
│       │       ├── file_name: skull-sparkle.svg
│       │       ├── file_type: .svg
│       │       ├── file_stats
│       │       │   ├── bytes: 1875
│       │       │   ├── last_modified_utc: 1698362088.4163365
│       │       │   ├── last_accessed_utc: 1698362088.5786703
│       │       │   └── created_utc: 1698362088.4163365
│       │       └── content: <?xml version="1.0" encoding="utf-8"?>
│       │           <!-- Generator: Adobe Illustrator 26.5.0, SVG Export Plug-In
│       │           ...
│       │           6c3,0,5.2-3,5.5-8.1c5.5-67.4,7.5-69.1,52.9-80.2C626.2,190.4,
│       │           628.4,187.6,628.4,182.6z"/>
│       │           </g>
│       │           </svg>
│       │           
│       ├── circle-exclamation-solid.svg
│       │   ├── type: file
│       │   └── content
│       │       ├── file_name: circle-exclamation-solid.svg
│       │       ├── file_type: .svg
│       │       ├── file_stats
│       │       │   ├── bytes: 494
│       │       │   ├── last_modified_utc: 1698362088.4158602
│       │       │   ├── last_accessed_utc: 1698362088.57776
│       │       │   └── created_utc: 1698362088.4158602
│       │       └── content: <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 
│       │           0 512 512"><!--! Font Awesome Pro 6.2.1 by @fonta
│       │           ...
│       │           13.3 10.7-24 24-24zm32 224c0 17.7-14.3 32-32 
│       │           32s-32-14.3-32-32s14.3-32 32-32s32 14.3 32 32z"/></svg>
│       ├── skull-solid.svg
│       │   ├── type: file
│       │   └── content
│       │       ├── file_name: skull-solid.svg
│       │       ├── file_type: .svg
│       │       ├── file_stats
│       │       │   ├── bytes: 666
│       │       │   ├── last_modified_utc: 1698362088.4162116
│       │       │   ├── last_accessed_utc: 1698362088.5780797
│       │       │   └── created_utc: 1698362088.4162116
│       │       └── content: <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 
│       │           0 512 512"><!--! Font Awesome Pro 6.2.1 by @fonta
│       │           ...
│       │           -64s64 28.7 64 64zm128 64c-35.3 0-64-28.7-64-64s28.7-64 
│       │           64-64s64 28.7 64 64s-28.7 64-64 64z"/></svg>
│       ├── pencil-solid.svg
│       │   ├── type: file
│       │   └── content
│       │       ├── file_name: pencil-solid.svg
│       │       ├── file_type: .svg
│       │       ├── file_stats
│       │       │   ├── bytes: 863
│       │       │   ├── last_modified_utc: 1698362088.4159808
│       │       │   ├── last_accessed_utc: 1698362088.5766485
│       │       │   └── created_utc: 1698362088.4159808
│       │       └── content: <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 
│       │           0 512 512"><!--! Font Awesome Pro 6.2.1 by @fonta
│       │           ...
│       │           c-6.2 6.2-16.4 6.2-22.6 0s-6.2-16.4 0-22.6l144-144c6.2-6.2 
│       │           16.4-6.2 22.6 0s6.2 16.4 0 22.6z"/></svg>
│       ├── skull-smile.svg
│       │   ├── type: file
│       │   └── content
│       │       ├── file_name: skull-smile.svg
│       │       ├── file_type: .svg
│       │       ├── file_stats
│       │       │   ├── bytes: 1295
│       │       │   ├── last_modified_utc: 1698362088.4160979
│       │       │   ├── last_accessed_utc: 1698362088.5718973
│       │       │   └── created_utc: 1698362088.4160979
│       │       └── content: <?xml version="1.0" encoding="utf-8"?>
│       │           <!-- Generator: Adobe Illustrator 26.5.0, SVG Export Plug-In
│       │           ...
│       │           .5-4.7-8.9-10c5-47,44.7-83.5,93-83.5s88,36.6,93,83.5C451.8,2
│       │           67.8,447.6,272.5,442.3,272.5z"/>
│       │           </svg>
│       │           
│       └── blender_icon.svg
│           ├── type: file
│           └── content
│               ├── file_name: blender_icon.svg
│               ├── file_type: .svg
│               ├── file_stats
│               │   ├── bytes: 1258
│               │   ├── last_modified_utc: 1698362088.4157305
│               │   ├── last_accessed_utc: 1698362088.5798254
│               │   └── created_utc: 1698362088.4157305
│               └── content: <svg fill="#000000" 
│                   xmlns="http://www.w3.org/2000/svg"  viewBox="0 0 50 50" 
│                   width="50px" height="50p
│                   ...
│                   998938 20 30.960938 20 z M 30.960938 22 A 6 5 0 0 0 
│                   30.960938 32 A 6 5 0 0 0 30.960938 22 z"/></svg>
├── stylesheets/
│   └── extra.css
│       ├── type: file
│       └── content
│           ├── file_name: extra.css
│           ├── file_type: .css
│           ├── file_stats
│           │   ├── bytes: 2294
│           │   ├── last_modified_utc: 1698362088.42935
│           │   ├── last_accessed_utc: 1698362090.2483594
│           │   └── created_utc: 1698362088.42935
│           └── content: 
│               
│               :root {
│                 --md-admonition-icon--tip-full-width: 
│               url('../assets/icons/skull-sparkle.svg')
│               }
│               .md-typ
│               ...
│               e: var(--md-admonition-icon--finished);
│                         mask-image: var(--md-admonition-icon--finished);
│               }
└── getting_started/
    ├── software_hardware_prerequisites.md
    │   ├── type: file
    │   └── content
    │       ├── file_name: software_hardware_prerequisites.md
    │       ├── file_type: .md
    │       ├── file_stats
    │       │   ├── bytes: 2071
    │       │   ├── last_modified_utc: 1698362088.428866
    │       │   ├── last_accessed_utc: 1698362089.6212747
    │       │   └── created_utc: 1698362088.428866
    │       └── content: # Prerequisites for Using FreeMoCap
    │           
    │           ## 1. Required Equipment
    │           
    │           The absolute minimum required equipme
    │           ...
    │            We'll have a section for the installation process and standard 
    │           troubleshooting in another section.
    │           
    ├── setting_up_environment.md
    │   ├── type: file
    │   └── content
    │       ├── file_name: setting_up_environment.md
    │       ├── file_type: .md
    │       ├── file_stats
    │       │   ├── bytes: 3166
    │       │   ├── last_modified_utc: 1698362088.4285939
    │       │   ├── last_accessed_utc: 1698362088.6268635
    │       │   └── created_utc: 1698362088.4285939
    │       └── content: 
    │           ## Lighting Conditions
    │           
    │           Lighting is crucial for a camera-based system like FreeMoCap. 
    │           For best resu
    │           ...
    │           ting. A successful calibration is also necessary, which will be 
    │           covered in a separate how-to guide.
    │           
    ├── single_camera_recording.md
    │   ├── type: file
    │   └── content
    │       ├── file_name: single_camera_recording.md
    │       ├── file_type: .md
    │       ├── file_stats
    │       │   ├── bytes: 2490
    │       │   ├── last_modified_utc: 1698362088.4287355
    │       │   ├── last_accessed_utc: 1698362089.2629158
    │       │   └── created_utc: 1698362088.4287355
    │       └── content: ## Single-Camera Recording
    │           
    │           ### Introduction
    │           We recommend that everybody starts by creating a single
    │           ...
    │           p a Blender scene if Blender was properly detected and populate 
    │           the folder with the output files!
    │           
    │           
    │           
    ├── index.md
    │   ├── type: file
    │   └── content
    │       ├── file_name: index.md
    │       ├── file_type: .md
    │       ├── file_stats
    │       │   ├── bytes: 302
    │       │   ├── last_modified_utc: 1698362088.4279928
    │       │   ├── last_accessed_utc: 1698362089.236391
    │       │   └── created_utc: 1698362088.4279928
    │       └── content: ``` mermaid
    │           graph TD
    │               A1(1. Installation)
    │               A1-->A(Create New Recording)
    │               A --if single came
    │           ...
    │              
    │               B --> F(3D Reconstruction)    
    │               F --> H(Post Processing)
    │               H --> I(Visualization)
    │           ```
    │           
    │           
    ├── multi_camera_calibration.md
    │   ├── type: file
    │   └── content
    │       ├── file_name: multi_camera_calibration.md
    │       ├── file_type: .md
    │       ├── file_stats
    │       │   ├── bytes: 2103
    │       │   ├── last_modified_utc: 1698362088.428316
    │       │   ├── last_accessed_utc: 1698362088.625482
    │       │   └── created_utc: 1698362088.428316
    │       └── content: ## Multi-Camera Calibration Guide
    │           !!! tip
    │                [Check out this video for more information and direct
    │           ...
    │           elpful output, as the log at the bottom of the  GUI screen does 
    │           not capture all of the outputs yet.
    │           
    └── installation.md
        ├── type: file
        └── content
            ├── file_name: installation.md
            ├── file_type: .md
            ├── file_stats
            │   ├── bytes: 2014
            │   ├── last_modified_utc: 1698362088.4281385
            │   ├── last_accessed_utc: 1698362088.624059
            │   └── created_utc: 1698362088.4281385
            └── content: ___
                # QUICKSTART:
                In a Python 3.8 through 3.11 environment, enter: 
                ```
                pip install --pre freemocap 
                ...
                amera Calibration 
                Guide](getting_started/multi_camera_calibration/) guide) section
                for next steps!
                
                


```

