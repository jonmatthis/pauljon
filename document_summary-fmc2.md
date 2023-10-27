+++++++++++++++++++++++++++++++++++

INDIVIDUAL FILE PATH - scraped_docs_data/documentation/docs/troubleshooting.md

Explanation: This document can be categorized as an Explanation type of documentation in the Diataxis framework. It provides troubleshooting information and aims to help users gain a deeper understanding of specific problems and how to fix them.

-----------------------------------

+++++++++++++++++++++++++++++++++++

INDIVIDUAL FILE PATH - scraped_docs_data/documentation/docs/about_us.md

**Explanation: Understanding-oriented discussion to provide context and illuminate concepts. Help users gain deeper knowledge.**

The document titled "About Us" provides an explanation of the Free Motion Capture Project (FreeMoCap). It explains the project's goal of providing research-grade markerless motion capture software for free. The document also highlights the project's focus on creating a user-friendly framework that connects various open-source tools from the computer vision and machine learning communities. It emphasizes the aim of making these technologies accessible to a wide range of communities. The document discusses the project's development philosophy of "Universal Design" and its potential benefits for different user groups. It also includes an overview of the software, its features, and capabilities. Additionally, it mentions the community involvement and support available through a Discord server and GitHub. Overall, this document provides a deeper understanding of the project's objectives, technologies, and community engagement.

-----------------------------------

+++++++++++++++++++++++++++++++++++

INDIVIDUAL FILE PATH - scraped_docs_data/documentation/docs/index.md

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

INDIVIDUAL FILE PATH - scraped_docs_data/documentation/docs/terminology/terminology.md

# Explanation: Terminology

This document provides a brief explanation of the terminology used in the project. It includes definitions for "Capture Volume," "Calibration," "Charuco Board," "Mediapipe," and "Processing Stages." The document serves as a reference for users to find factual information about the project's terminology.

# Explanation: Capture Volume

Capture Volume refers to a 3-dimensional area with sufficient camera coverage to support 3D tracking. This concept is important for understanding how the project captures and analyzes motion data. 

# Explanation: Calibration

Calibration is the process of determining the location of each camera during a recording session and calibrating the capture volume. The document provides a link to a section of a video discussing capture volume calibration. Understanding calibration is crucial for accurate motion tracking.

# Explanation: Charuco Board

A Charuco Board is a type of calibration board used in the project's calibration process. The document provides a link to a section of a video discussing capture volume calibration, which includes information about Charuco Boards.

# Reference: Mediapipe

Mediapipe is a solution used in the project for tracking 2D points in videos and reconstructing 3D data. The document provides a link to the Mediapipe documentation for users to find more information.

# Explanation: Processing Stages

This section provides a brief description of each processing stage necessary to use USB webcams for 3D motion capture. The stages include recording videos, synchronizing videos, calibrating the capture volume, tracking 2D points, reconstructing 3D data, using Blender for output data files (optional), and saving skeleton animation. Understanding these stages is essential for users to successfully utilize the project's capabilities.

# Explanation: Reprojection Error

Reprojection Error refers to the distance between the originally measured 2D point (skeleton) and the reconstructed 3D point reprojected back onto the image plane. The document explains that a reprojection error of zero indicates perfect 3D reconstruction and 2D tracking. It also discusses possible causes of reprojection error, such as inaccurate 2D tracks or bad camera calibration. The document provides a link to a Discord conversation for further discussion on this topic.

Overall, this document serves as a reference for users to understand the project's terminology, capture volume, calibration, processing stages, and reprojection error. It provides factual information and context to help users gain a deeper knowledge of the project.

-----------------------------------

+++++++++++++++++++++++++++++++++++

INDIVIDUAL FILE PATH - scraped_docs_data/documentation/docs/contributing/feature_request.md

**Document Type: How-To Guide**

**Summary:**
This document serves as a guide for users who want to propose new ideas and feature requests for the project. It provides instructions on how to open a new issue on GitHub and includes the necessary details to include in the request. The document also emphasizes that not all requested features may be implemented, but each request will be considered and prioritized based on project and community needs.

-----------------------------------

+++++++++++++++++++++++++++++++++++

INDIVIDUAL FILE PATH - scraped_docs_data/documentation/docs/contributing/python_code_style_guide.md

DOCUMENT TYPE: Explanation

SUMMARY: 
This document provides guidelines for maintaining code readability, quality, and maintainability. It covers general guidelines such as following a Universal Design approach and adhering to PEP 8 Guidelines. It also includes specific guidelines for using Google-formatted docstrings, type hints, keyword arguments, private methods and attributes, descriptive names, PEP8 and `black` formatting, consistent naming conventions, keeping functions and methods short, modularizing code, minimizing comments, error handling, writing tests, and performing code reviews. This document serves as an understanding-oriented discussion to provide context and illuminate concepts related to maintaining code quality and best practices.

-----------------------------------

+++++++++++++++++++++++++++++++++++

INDIVIDUAL FILE PATH - scraped_docs_data/documentation/docs/contributing/bug_report.md

### How-To Guide: Writing Detailed Bug Reports

Bug reports are an essential part of the software development process as they help identify and resolve issues. This document provides guidance on how to write detailed bug reports that effectively communicate the problem to the community and maintainers.

To create a "great" bug report, consider the following:

1. Quick summary and background: Provide a brief overview of the issue and any relevant context. This helps readers quickly understand the problem.

2. Steps to reproduce: Be specific and provide clear instructions on how to reproduce the bug. Include any necessary files or data that are required to replicate the issue. For example, if the bug occurs during a specific session, upload the ZIP file of that session.

3. Sample code: If possible, include sample code that demonstrates the issue. This can be helpful for others to understand the problem and potentially find a solution. Referencing external resources, such as a Stack Overflow question, where the user provides detailed information, can also be beneficial.

4. Expected vs actual behavior: Clearly state what you expected to happen and what actually happens when the bug occurs. This helps others identify the deviation from expected behavior.

5. Notes: Include any additional information that may be relevant, such as your thoughts on why the bug might be happening or any unsuccessful attempts to resolve it. This can provide valuable insights to the community and maintainers.

Remember, thorough bug reports increase the likelihood of receiving assistance from the community and maintainers. By following these guidelines, you can effectively communicate the problem and contribute to the improvement of the software.

-----------------------------------

+++++++++++++++++++++++++++++++++++

INDIVIDUAL FILE PATH - scraped_docs_data/documentation/docs/contributing/index.md

# Explanation: Contributing to the FreeMoCap Project

This document provides guidance on how to contribute to the FreeMoCap project. It covers various aspects such as reporting bugs, suggesting new features, and submitting code changes. The document is aimed at users who want to actively participate in the project's development.

## Tutorials: Getting Started

This section provides instructions on how to get started with FreeMoCap, including installing it from source code. It serves as a learning-oriented guide for users who are new to the project and need assistance in setting up the software.

## How-To Guides: Reporting Bugs and Suggesting Features

The document explains how users can report bugs and suggest new features for FreeMoCap. It provides step-by-step instructions and links to relevant guides for reporting bugs and making feature requests. This section serves as a task-oriented guide to help users solve specific problems they encounter while using the software.

## How-To Guides: Code Contributions

This section focuses on contributing code to FreeMoCap. It explains the development process, coding styles, and testing requirements. Users will learn how to create and submit pull requests, ensuring that their code meets the project's standards. This section serves as a task-oriented guide to help users accomplish the specific goal of contributing code changes.

## Reference: Coding Styles and Testing

The document provides references to coding style guides for the FreeMoCap project, including Python code style. It also emphasizes the importance of testing and provides resources for learning about testing in Python. This section serves as an information-oriented technical description to help users find factual information about coding styles and testing practices.

## How-To Guides: Getting Help and Asking Questions

The document concludes with information on how users can seek help and ask questions related to FreeMoCap. It suggests reaching out on the project's Discord server or creating a new issue on GitHub. This section serves as a task-oriented guide to help users solve the problem of seeking assistance and obtaining the information they need.

Overall, this document covers a range of topics related to contributing to the FreeMoCap project. It provides learning-oriented tutorials, task-oriented how-to guides, information-oriented references, and understanding-oriented explanations to cater to different user needs at various stages of their journey with the software.

-----------------------------------

+++++++++++++++++++++++++++++++++++

INDIVIDUAL FILE PATH - scraped_docs_data/documentation/docs/community/code_of_conduct.md

DOCUMENT SUMMARY:

This document is a Code of Conduct for the project's community. It sets the standards for behavior and aims to create an open and welcoming environment for all participants. It emphasizes the importance of using inclusive language, respecting differing viewpoints, accepting constructive criticism, and focusing on the best interests of the community. It also outlines examples of unacceptable behavior, such as harassment and the use of inappropriate language or imagery. The document encourages conflict resolution through respectful dialogue and offers contact information for assistance if needed. 

This document falls under the "Reference" type of documentation as it provides information-oriented technical descriptions of the project's community standards. It helps users find factual information about the expected behavior and conduct within the community.

-----------------------------------

+++++++++++++++++++++++++++++++++++

INDIVIDUAL FILE PATH - scraped_docs_data/documentation/docs/community/privacy_policy.md

# Explanation: Privacy Policy

This document provides an explanation of the privacy policy for our software. It outlines how we collect, use, and protect personal or anonymous data from users. The document is aimed at providing users with a deeper understanding of our privacy practices and their control over their data.

The document falls under the "Explanation" type of documentation in the Diataxis framework. It serves the user need for understanding and gaining deeper knowledge about our privacy policy and data handling practices.

The document starts by introducing the purpose of the privacy policy and clarifying the terms used. It then explains the collection of anonymous user data, including the information collected and how it is sent to us. It provides links to the code responsible for collecting the data.

The document also emphasizes the protection of user data and our commitment to not sell or distribute it to third parties, except as required by law. It mentions the security measures in place and the limited access to user data by core developers.

Users are informed about their control over their data, including the option to turn off data collection and the process for requesting data deletion.

The document concludes with a statement about possible updates to the privacy policy and provides contact information for any questions or concerns.

Overall, this document provides an in-depth explanation of our privacy policy and data handling practices, helping users gain a deeper understanding of how their data is collected, used, and protected.

-----------------------------------

+++++++++++++++++++++++++++++++++++

INDIVIDUAL FILE PATH - scraped_docs_data/documentation/docs/getting_started/software_hardware_prerequisites.md

### Document Type: Tutorials - Learning-oriented guides that provide lessons to teach users basic skills. Help users get started.

### Summary:
This document provides the prerequisites for using FreeMoCap, a software for reconstructing movement data. It outlines the required equipment, such as cameras and a Charuco board for calibration, as well as the necessary software, including Blender and optional tools like VS Code or JupyterLab. The document also mentions the recommended installation method and future plans for software download options. Overall, this document serves as a guide for users who are new to FreeMoCap and need to understand what they need to get started.

-----------------------------------

+++++++++++++++++++++++++++++++++++

INDIVIDUAL FILE PATH - scraped_docs_data/documentation/docs/getting_started/setting_up_environment.md

**Document Type: How-To Guide**

**Summary:**
This document provides guidance on setting up the environment for FreeMoCap, a camera-based system. It emphasizes the importance of lighting conditions and suggests using bright environments for optimal results. It explains the concept of exposure time and how it affects motion blur and the identification of subject joints. The document also discusses background considerations, such as using a solid-colored backdrop and subjects wearing tight-fitting clothes. Additionally, it provides recommendations for camera placement and configuration in multi-camera setups, including capturing a standing human in a tighter space and separating cameras to improve triangulation. The document highlights the need for adjusting camera settings and successful calibration for high-quality recordings, which will be covered in a separate how-to guide.

-----------------------------------

+++++++++++++++++++++++++++++++++++

INDIVIDUAL FILE PATH - scraped_docs_data/documentation/docs/getting_started/single_camera_recording.md

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

INDIVIDUAL FILE PATH - scraped_docs_data/documentation/docs/getting_started/index.md

This document can be classified as a tutorial in the Diataxis Documentation framework. It provides a step-by-step guide for users to get started with the software. The document starts with installation instructions and then walks users through the process of creating a new recording, recording videos, calibrating the capture volume, performing 3D reconstruction, post-processing, and visualization. This tutorial is aimed at helping users learn the basic skills required to use the software effectively.

-----------------------------------

+++++++++++++++++++++++++++++++++++

INDIVIDUAL FILE PATH - scraped_docs_data/documentation/docs/getting_started/multi_camera_calibration.md

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

INDIVIDUAL FILE PATH - scraped_docs_data/documentation/docs/getting_started/installation.md

# TUTORIAL: Installation

This document provides a step-by-step guide to help users get started with the installation of the software. It falls under the "Tutorials" category of the Diataxis Documentation framework. The goal of this document is to teach users the basic skills required to install the software.

The document begins with a quickstart section that provides a concise command to install the software. It then proceeds to explain the installation process in detail, including instructions for opening a terminal window and creating a new Python environment. The document also provides alternative installation methods using PyPi (pip) and GitHub.

Once the installation is complete, users are instructed to launch the GUI. The document concludes by directing users to the Single-Camera Tutorial and Multi-Camera Calibration Guide for further steps.

Overall, this document serves the user need of learning how to install the software and get started with it. It aligns with the pragmatic improvement goal of the Diataxis Documentation framework by providing a clear and organized guide for users.

-----------------------------------

=============================================================

=============================================================



 GLOBAL SUMMARY OF SUMMARIES 
 
=============================================================

 Here is a summary report of the current state of the documentation for the open source software project:

## Identification of Gaps Based on Diataxis Framework

After reviewing the existing documentation, here are some gaps that would help complete an approach aligned with the Diataxis Documentation framework:

**Theory Documentation**
- Explanation of the computer vision and machine learning concepts and algorithms behind the core functionality. This would help provide deeper understanding.

**Practical Documentation** 
- Step-by-step guides for common use cases beyond the getting started tutorial, such as recording with multiple asynchronous cameras.
- Troubleshooting guides for common issues and errors.
- More details on customizing and configuring the software for different needs.

**Acquisition Documentation**
- More conceptual overview of the software architecture and components. 
- API reference documentation.

**Application Documentation**
- More examples and case studies demonstrating real-world application of the software.
- Guidance on analyzing and interpreting output data.

## Prioritized List of Existing Docs and Gaps

**High Priority**

- Getting Started Tutorials - exist and provide a good starting point
- Multi-camera calibration guide - exists but could be expanded 
- Troubleshooting guide - does not exist but would be very useful

**Medium Priority** 

- Explanation articles on core concepts - do not exist but would improve understanding
- Customization/configuration guides - some basics exist but more details needed
- Asynchronous camera guide - does not exist

**Lower Priority**

- API reference - does not exist 
- Real-world examples and case studies - do not exist
- Data analysis guidance - does not exist

In summary, the highest priorities based on gaps in the Diataxis framework are troubleshooting guides, conceptual explanations, and configuration/customization guides. Filling these gaps would most improve the usefulness and completeness of the documentation.

