+++++++++++++++++++++++++++++++++++

- Diátaxis is the work of Daniele Procida.
- The principles described in this website have been developed over a number of years and continue to be elaborated and explored.
- The original context for this approach was software product documentation.
- More recent work has seen them applied at scale in internal corporate documentation, scientific research contexts, organizational management, and education.
- The key concepts behind Diátaxis first crystallized while working at Divio, the cloud applications platform.
- The ideas were presented at conferences in early 2017 and later written up as "The documentation system" for Divio.
- The thinking and approaches developed at Divio are at the core of the Diátaxis documentation philosophy.
- Since leaving Divio in 2021, Daniele Procida has continued to research and refine their approaches and methods in documentation.
- The material published at https://documentation.divio.com/ is Divio's intellectual property.
- Contact the author, Daniele Procida, via email or through the Write the Docs Slack group or GitHub repository.
- To cite Diátaxis, refer to the website or the citation file in the Git repository.
- The website is built with Sphinx and hosted on Read the Docs, using a modified version of the Furo theme by Pradyun Gedam.

-----------------------------------

+++++++++++++++++++++++++++++++++++

- The Diátaxis framework is a lightweight and flexible architecture for technical documentation.
- It has been adopted by various projects and organizations, including IBM LoopBack, Cloudflare, Gatsby, Django, and Canonical.
- The framework provides four quadrants to prioritize the user's goal for each type of documentation.
- Projects and organizations that have adopted the framework include Aiven Developer, BBC News Labs, BrachioGraph, BeeWare, Bosch, Ciw, clj-otel, Cloudflare Workers docs, corrux, Divio, django CMS, edo, Encore, Ericsson, fpm, Google's Fuchsia operating system, Funding Circle, Gensim, Gorgonia, gtk-fortran, ING Bank, Lisk, Livepeer, LootLocker, Matching, NashPy, nbchkr, NumPy, PDFminer.six, PostgREST, PIconnect, Snowpack, Sourcegraph, Splink, stdlib, StrongLoop/LoopBack by IBM, TerminusDB, Tesla Motors, WebAccess/DMP, websockets, Wechaty, and Zalando.
- Other mentions and references of interest include Django Axes proposal, GitLab's Data Team documentation guide, Julia language proposal, Why You Should Document Your Work As a Data Scientist, Koninglijke Biblioteek research software lab, Tutorials in Jenkins user documentation, and TYPO3.

-----------------------------------

+++++++++++++++++++++++++++++++++++

- The Diátaxis framework solves a problem of quality in technical documentation.
- It describes an information architecture that makes it easier to create, maintain, and use documentation.
- Diátaxis identifies four modes of documentation: tutorials, how-to guides, technical reference, and explanation.
- Each mode corresponds to a different user need and requires a different approach to its creation.
- Technical documentation should be structured explicitly around these four types and keep them separate and distinct from each other.
- Understanding the implications of these four different types of documentation can help improve most documentation.
- Diátaxis is light-weight, easy to understand, and straightforward to apply.
- It doesn't impose implementation constraints and brings an active principle of quality to documentation.
- Diátaxis is proven in practice across a wide variety of fields and applications in both open and proprietary documentation projects.

-----------------------------------

+++++++++++++++++++++++++++++++++++

- Explanation is discussion that clarifies and illuminates a particular topic, focusing on understanding-oriented information.
- It deepens and broadens the reader's understanding of a subject.
- Explanation is not concerned with user actions or close-up views of the machinery.
- It approaches a topic from a higher perspective and different angles.
- Explanation is valuable and important for practitioners to have a comprehensive understanding of their craft.
- It can be called "Discussion," "Background," "Conceptual guides," or "Topics."
- Explanation is often scattered in small parcels in other sections of documentation.
- Writing good explanation involves making connections to other topics, providing background and context, discussing alternatives and opinions, and avoiding instruction or technical reference.
- The language of explanation includes explaining historical reasons, offering judgments and opinions, providing context, weighing up alternatives, and unfolding the internal secrets of the machinery.

-----------------------------------

+++++++++++++++++++++++++++++++++++

- Reference guides are technical descriptions of the machinery and how to operate it.
- Reference material is information-oriented and serves as a firm platform for users to work on.
- Reference guides describe the software itself, such as APIs, classes, and functions.
- Reference material should be austere and to the point, with no ambiguity or doubt.
- Reference material is like a map, providing information about the product and its internal machinery.
- Some reference material can be generated automatically by the software, ensuring accuracy.
- Reference material should provide accurate, up-to-date, and comprehensive information.
- Reference material should respect the structure of the product, mirroring its architecture.
- Consistency in structure, language, terminology, and tone is important in reference material.
- Technical reference should focus solely on describing the machinery and avoid explaining or instructing.
- Examples can be used to illustrate usage and provide context in reference material.
- Accuracy is crucial in reference material to avoid leading users astray.
- The language of reference guides should state facts, list commands and options, and provide warnings where appropriate.

-----------------------------------

+++++++++++++++++++++++++++++++++++

- How-to guides are directions that take the reader through the steps required to solve a real-world problem.
- How-to guides are goal-oriented and serve as practical steps to achieve a specific end.
- Examples of how-to guides include calibrating a radar array, using fixtures in pytest, and configuring reconnection back-off policies.
- How-to guides are distinct from tutorials and serve different user needs.
- How-to guides should be written in a sequence of actions with a clear order.
- The focus of a how-to guide should be on solving a specific problem or task.
- How-to guides should not include explanations and should be flexible to adapt to real-world use-cases.
- Practical usability is more important than completeness in how-to guides.
- Choosing clear and specific titles for how-to guides is important.
- The language of how-to guides should describe the problem or task clearly, use conditional imperatives, and avoid including every possible thing the user might do related to a topic.

-----------------------------------

+++++++++++++++++++++++++++++++++++

- Diátaxis is an approach to quality in documentation.
- Quality in documentation is often not clearly defined.
- There are two types of quality in documentation: functional quality and deep quality.
- Functional quality includes accuracy, completeness, consistency, usefulness, and precision.
- Deep quality includes characteristics such as feeling good to use, having flow, fitting to human needs, being beautiful, and anticipating the user.
- Functional quality can be objectively measured, while deep quality is subjective and can only be judged.
- Deep quality is conditional upon functional quality.
- Deep quality represents liberation and creativity, while functional quality represents constraints.
- Deep quality and functional quality have independent characteristics.
- Deep quality is subjective and assessed against the human, while functional quality is objective and measured against the world.
- Deep quality can be recognized by the feeling of pleasure and satisfaction when using documentation.
- Diátaxis cannot address functional quality but can expose lapses in it.
- Diátaxis can help documentation fit user needs and maintain flow.
- Diátaxis is not a guarantee of deep quality but lays down conditions for its possibility.

-----------------------------------

+++++++++++++++++++++++++++++++++++

- The Diátaxis Documentation framework is a way of structuring documentation for a software project.
- The basic structure of the framework includes a landing page, tutorial, how-to guides, reference, and explanation sections.
- Each section has an overview landing page that provides an overview of the contents within.
- A layer of hierarchy can be added to group pages within sections, such as different installation options.
- Lists longer than a few items should be broken up into smaller ones to improve readability.
- Landing pages should read like an overview and introduce the content within.
- The framework can handle complex hierarchies and different user types by organizing documentation based on their specific needs.
- The structure of the documentation should be based on user needs and should not be limited to the four categories of the framework.
- The Diátaxis approach focuses on user-first thinking and attention to user needs.
- Documentation should be as complex as necessary but should still be logical and incorporate patterns that fit user needs.

-----------------------------------

+++++++++++++++++++++++++++++++++++

- The Diataxis Documentation framework is licensed under the Creative Commons Attribution-ShareAlike 4.0 International Public License.
- The framework provides a standard set of terms and conditions for sharing original works of authorship and other material subject to copyright.
- Licensors should read and understand the terms and conditions of the license before applying it and should secure all necessary rights before applying the license.
- The public can use the licensed material under specified terms and conditions, but the license only grants permissions under copyright and certain other rights.
- The framework allows for adaptations of the licensed material, which must be shared under the same license or a compatible license.
- The framework includes conditions for attribution and sharing adaptations.
- The Licensor offers the licensed material as-is and makes no warranties regarding its use.
- The Licensor is not liable for any damages resulting from the use of the licensed material.
- The license terminates automatically if the licensee fails to comply with its terms.
- The Licensor may offer the licensed material under separate terms or conditions or stop distributing it at any time.
- The framework does not impose conditions on any use of the licensed material that could be made without permission.
- Creative Commons is not a party to the public licenses but may apply them to material it publishes.

-----------------------------------

+++++++++++++++++++++++++++++++++++

- Tutorials are lessons that guide the reader through a series of steps to complete a project.
- Tutorials are learning-oriented and aim to help beginners achieve basic competence with a product.
- Tutorials should show learners that they can be successful with the product by having them do something meaningful and attainable.
- A tutorial is a lesson concerned with learning how, not learning that, and focuses on practical knowledge.
- A tutorial should enable the learner to make sense of the rest of the documentation and the product itself.
- Tutorials turn new learners into users of a product.
- The teacher has the responsibility for what the pupil will learn and do, while the pupil's only obligation is to follow the teacher's directions.
- A tutorial needs to be meaningful, successful, logical, and provide a complete encounter with the necessary actions, concepts, and tools.
- Tutorials are often the weakest part of documentation and require a significant amount of work to create and maintain.
- Writing and maintaining tutorials can be as time-consuming as all other parts of documentation combined.
- Tutorials are subject to frequent revisions due to product changes and the need for improved learning experiences.
- Teaching a child to cook demonstrates the demands imposed by a tutorial, where the focus is on the child enjoying the experience and gaining confidence.
- A good tutorial allows the user to learn by doing and provides clear instructions for performing actions and using tools.
- The goal of a tutorial is to get the learner started, not to turn them into an expert.
- Tutorials should provide a complete picture of what the learner will achieve before they start.
- Tutorials should work reliably and inspire the learner's confidence by ensuring that the instructions produce the promised results.
- Learners should see results immediately and understand the cause and effect relationship of their actions.
- Tutorials should be repeatable for users with different skill levels, tools, and environments.
- Tutorials should focus on concrete steps rather than abstract concepts and avoid unnecessary explanations.
- Only provide the minimum necessary explanation for completing the tutorial.
- Ignore options and alternatives that are not required to reach the tutorial's conclusion.
- Use clear and specific language in tutorials, describing what the learner will accomplish and providing clues and reminders to help them stay on track.
- Celebrate the learner's accomplishments in the tutorial descriptions.

-----------------------------------

+++++++++++++++++++++++++++++++++++

- The Diataxis Documentation framework is a comprehensive and practical system designed to assist maintainers of product documentation.
- The framework is published at https://diataxis.fr and is authored by Daniele Procida.
- The framework is licensed under the CC-BY-SA 4.0 license.
- The framework aims to provide a structured and organized approach to maintaining product documentation.
- It offers guidelines and best practices for creating and managing documentation.
- The framework includes templates and examples to help maintainers create consistent and high-quality documentation.
- It provides tools and resources to streamline the documentation process and improve collaboration among maintainers.
- The framework emphasizes the importance of clear and concise documentation that is easily accessible to users.
- It encourages maintainers to regularly update and improve documentation to ensure its accuracy and relevance.
- The framework promotes the use of documentation as a means to enhance user experience and support product adoption.
- It provides guidance on documenting different aspects of a product, including installation, configuration, usage, and troubleshooting.
- The framework encourages maintainers to actively engage with users and gather feedback to continuously improve the documentation.
- It emphasizes the importance of documentation as a valuable resource for both maintainers and users of the product.

-----------------------------------

+++++++++++++++++++++++++++++++++++

- Tutorials and how-to guides are different in the Diátaxis documentation framework.
- Tutorials are learning-oriented and aim to provide a successful learning experience.
- How-to guides are task-oriented and aim to help the user accomplish a specific task.
- Tutorials familiarize the learner with the work and provide a structured, repeatable encounter.
- How-to guides assume familiarity with the tools, language, and processes.
- Tutorials eliminate the unexpected, while how-to guides prepare for the unexpected.
- Tutorials follow a carefully-managed path, while how-to guides can fork and branch.
- Tutorials must be safe, while how-to guides cannot promise safety.
- Responsibility lies with the teacher in tutorials, while the user has responsibility in how-to guides.
- Tutorials teach basic things explicitly, while how-to guides rely on implicit knowledge.
- Tutorials are concrete and particular, while how-to guides take a general approach.
- Tutorials teach general skills and principles, while how-to guides focus on completing a particular task.
- The difference between tutorials and how-to guides is based on the distinction between study and work.
- Tutorials are for learners, while how-to guides are for already-skilled practitioners.
- Tutorials can cover basic procedures, and how-to guides can cover complex or advanced topics.
- Understanding the distinction between tutorials and how-to guides is crucial for successful documentation.
- Conflating tutorials and how-to guides can lead to inconvenience and dissatisfaction for users.
- Getting the distinction right is key to the success of the documentation and the product.

-----------------------------------

+++++++++++++++++++++++++++++++++++

- Explanation and reference are both part of the theoretical knowledge in the Diataxis Documentation framework.
- Explanation is the acquisition of knowledge and skill, while reference is the application of knowledge and skill.
- Reference material is typically boring and unmemorable, while explanation material is more engaging.
- Lists of things and tables of information belong in reference material.
- If you can imagine reading something in the bath, it is likely explanation material.
- It is important to distinguish between reference and explanation, as they serve different needs of the reader.
- Reference material helps users apply knowledge and skill while working.
- Explanation material helps users acquire knowledge and skill through study.

-----------------------------------

+++++++++++++++++++++++++++++++++++

- The Diataxis Documentation framework aims to provide a clear and general structure for organizing documentation.
- The framework uses a two-dimensional map to describe different types of documentation and their relationships.
- The map is based on a systematic analysis of user needs, specifically the needs of practitioners in a specific domain of skill.
- Documentation is divided into four categories: tutorials, how-to guides, technical reference, and explanation.
- Tutorials introduce and educate, how-to guides guide and demonstrate, technical reference states and describes, and explanation explains and clarifies.
- Each category of documentation serves a specific purpose and is oriented towards either learning, tasks, information, or understanding.
- The framework provides clear expectations for readers and guidance for authors on how to write and place content.
- There is a natural tendency for the distinctions between different forms of documentation to blur, leading to structural problems.
- The framework is designed to support users in their cycle of interaction with a product, which includes learning, task-oriented work, consulting technical reference, and reflecting on practice and knowledge.

-----------------------------------

+++++++++++++++++++++++++++++++++++

- The Diátaxis map is a reminder of different types of documentation and their relationship.
- Intuition is not always reliable when determining the form of documentation needed.
- The Diátaxis compass is a decision-making tool for documentation.
- The compass reduces complex problems and provides course-correction.
- The compass consists of a list-table with different scenarios and corresponding documentation types.
- Practical steps that serve the user's study require a tutorial.
- Practical steps that serve the user's work require a how-to guide.
- Theoretical knowledge that serves the user's work requires a reference.
- Theoretical knowledge that serves the user's study requires an explanation.
- The compass can be applied to user situations or to improve existing documentation.
- Two questions need to be asked when using the compass: practical steps or theoretical knowledge, and study or work.
- The compass becomes more effective with practice.

-----------------------------------

+++++++++++++++++++++++++++++++++++

- Diátaxis is a documentation framework that aims to improve documentation for users and make it easier for creators to maintain.
- It is meant to be used as a guide, not a strict plan, to help assess and improve documentation.
- The focus should be on making improvements based on Diátaxis principles, rather than worrying about the structure.
- Documentation should be improved iteratively, taking small steps in the right direction.
- Instead of starting from scratch, choose a small piece of documentation to assess and make immediate improvements.
- Work should flow in the right direction without the need for a detailed plan.
- Documentation should develop organically, following the principles of well-formed organic growth.
- Documentation is never finished, but it can always be complete and appropriate for its current stage of development.

-----------------------------------

=============================================================

=============================================================

___ 
 > Global Summary 
  Here is a summary of the Diataxis Documentation framework in a bulleted list:

- Tutorials - Learning-oriented guides that provide lessons to teach users basic skills. Help users get started.

- How-To Guides - Task-oriented guides that provide steps to accomplish specific goals. Help users solve problems. 

- Reference - Information-oriented technical descriptions of the product. Help users find factual information.

- Explanation - Understanding-oriented discussion to provide context and illuminate concepts. Help users gain deeper knowledge.

- The framework divides documentation into 4 types based on 2 axes:

    - Theory vs Practice

    - Acquisition vs Application

- Each type serves a distinct user need at different points in their journey using the product. 

- Keeping the types clearly separated improves quality by ensuring docs fit user needs.

- The framework provides a systematic approach to create, organize and maintain technical documentation.

- It can be adopted fully or partially depending on needs. The goal is pragmatic improvement.

- Start small, assess and improve one part at a time to steadily enhance overall documentation.

```

🌱
├── colofon.rst
│   ├── type: file
│   └── content
│       ├── file_name: colofon.rst
│       ├── file_type: .rst
│       ├── file_stats
│       │   ├── bytes: 3265
│       │   ├── last_modified_utc: 1698361445.8012261
│       │   ├── last_accessed_utc: 1698361445.9489908
│       │   └── created_utc: 1698361445.8012261
│       └── content: Colofon
│           ===================
│           
│           Diátaxis is the work of Daniele Procida.
│           
│           The principles described in t
│           ...
│            the
│           `Furo <https://github.com/pradyunsg/furo>`_ theme by `Pradyun Gedam
│           <https://pradyunsg.me/>`_.
│           
├── adoption.rst
│   ├── type: file
│   └── content
│       ├── file_name: adoption.rst
│       ├── file_type: .rst
│       ├── file_stats
│       │   ├── bytes: 6423
│       │   ├── last_modified_utc: 1698361445.801026
│       │   ├── last_accessed_utc: 1698361446.6041873
│       │   └── created_utc: 1698361445.801026
│       └── content: .. meta::
│              :description:
│                  Adopted by IBM LoopBack, Cloudflare and dozens of other 
│           products a
│           ...
│           YPO3 
│           <https://docs.typo3.org/m/typo3/docs-how-to-document/master/en-us/Wr
│           itingContent/Index.html>`_
│           
├── index.rst
│   ├── type: file
│   └── content
│       ├── file_name: index.rst
│       ├── file_type: .rst
│       ├── file_stats
│       │   ├── bytes: 3048
│       │   ├── last_modified_utc: 1698361445.8396664
│       │   ├── last_accessed_utc: 1698361446.6065564
│       │   └── created_utc: 1698361445.8396664
│       └── content: .. meta::
│              :description:
│                  The Diátaxis framework solves a problem of quality in 
│           technical do
│           ...
│           w-to-use-diataxis
│           
│           .. toctree::
│              :maxdepth: 1
│              :hidden:
│              :titlesonly:
│           
│              adoption
│              colofon
│           
├── requirements.txt
│   ├── type: file
│   └── content
│       ├── file_name: requirements.txt
│       ├── file_type: .txt
│       ├── file_stats
│       │   ├── bytes: 745
│       │   ├── last_modified_utc: 1698361445.8411264
│       │   ├── last_accessed_utc: 1698361446.030758
│       │   └── created_utc: 1698361445.8411264
│       └── content: alabaster==0.7.12
│           Babel==2.9.1
│           beautifulsoup4==4.10.0
│           certifi==2022.12.7
│           charset-normalizer==2.0.10
│           
│           ...
│           .5
│           sphinxcontrib-spelling==7.3.2
│           tornado==6.1
│           urllib3==1.26.8
│           zipp==3.7.0
│           sphinx-reredirects==0.1.2
│           
├── explanation.rst
│   ├── type: file
│   └── content
│       ├── file_name: explanation.rst
│       ├── file_type: .rst
│       ├── file_stats
│       │   ├── bytes: 6830
│       │   ├── last_modified_utc: 1698361445.8022203
│       │   ├── last_accessed_utc: 1698361445.9678495
│       │   └── created_utc: 1698361445.8022203
│       └── content: .. _explanation:
│           
│           About explanation
│           =================
│           
│           ..  rubric:: Explanation is **discussion** th
│           ...
│           .*
│               Unfold the machinery's internal secrets, to help understand why 
│           something does what it does.
│           
├── reference.rst
│   ├── type: file
│   └── content
│       ├── file_name: reference.rst
│       ├── file_type: .rst
│       ├── file_stats
│       │   ├── bytes: 5808
│       │   ├── last_modified_utc: 1698361445.8409061
│       │   ├── last_accessed_utc: 1698361446.6474535
│       │   └── created_utc: 1698361445.8409061
│       └── content: .. _reference:
│           
│           About reference
│           ======================
│           
│           ..  rubric:: Reference guides are **technica
│           ...
│           .
│           *You must use a. You must not apply b unless c. Never d.*
│               Provide warnings where appropriate.
│           
├── Makefile/
│   ├── type: file
│   └── content
│       ├── file_name: Makefile
│       ├── file_type: 
│       ├── file_stats
│       │   ├── bytes: 1646
│       │   ├── last_modified_utc: 1698361445.800182
│       │   ├── last_accessed_utc: 1698361445.957773
│       │   └── created_utc: 1698361445.800182
│       └── content: # You can set these variables from the command line.
│           SPHINXOPTS    =
│           SPHINXBUILD   = sphinx-build
│           SP
│           ...
│           r $(SPHINXOPTS).
│           %: Makefile
│                   @$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" 
│           $(SPHINXOPTS) $(O)
│           
├── CITATION.cff
│   ├── type: file
│   └── content
│       ├── file_name: CITATION.cff
│       ├── file_type: .cff
│       ├── file_stats
│       │   ├── bytes: 632
│       │   ├── last_modified_utc: 1698361445.799813
│       │   ├── last_accessed_utc: 1698361445.953385
│       │   └── created_utc: 1698361445.799813
│       └── content: # This CITATION.cff file was generated with cffinit.
│           # Visit https://bit.ly/cffinit to generate your
│           ...
│           d.org/0000-0001-5141-7509'
│             title: Diátaxis documentation framework
│             url: "https://diataxis.fr/"
│           
│           
├── conf.py
│   ├── type: file
│   └── content
│       ├── file_name: conf.py
│       ├── file_type: .py
│       ├── file_stats
│       │   ├── bytes: 2738
│       │   ├── last_modified_utc: 1698361779.4943979
│       │   ├── last_accessed_utc: 1698361780.7235157
│       │   └── created_utc: 1698361779.4943979
│       └── content: # Configuration file for the Sphinx documentation builder.
│           #
│           # This file only contains a selection o
│           ...
│           = tokenizer_lang = "en_GB"
│           
│           redirects = {
│                "citation": "/colofon",
│                "contact": "/colofon"
│           }
│           
├── how-to-guides.rst
│   ├── type: file
│   └── content
│       ├── file_name: how-to-guides.rst
│       ├── file_type: .rst
│       ├── file_stats
│       │   ├── bytes: 5992
│       │   ├── last_modified_utc: 1698361445.8025944
│       │   ├── last_accessed_utc: 1698361445.9730487
│       │   └── created_utc: 1698361445.8025944
│       └── content: .. _how-to:
│           
│           About how-to guides
│           ===================
│           
│           ..  rubric:: How-to guides are **directions** 
│           ...
│           Don't pollute your practical how-to guide with every possible thing 
│           the user might do related to x.
│           
├── spelling_wordlist.txt
│   ├── type: file
│   └── content
│       ├── file_name: spelling_wordlist.txt
│       ├── file_type: .txt
│       ├── file_stats
│       │   ├── bytes: 205
│       │   ├── last_modified_utc: 1698361445.8413541
│       │   ├── last_accessed_utc: 1698361446.7217326
│       │   └── created_utc: 1698361445.8413541
│       └── content: Colofon
│           Diátaxis
│           Dataset
│           backend
│           Ericsson
│           equilibria
│           Fortran
│           intubations
│           Jupyter
│           Chatbot
│           Zalando
│           Divio
│           Laing
│           δῐᾰ́τᾰξῐς
│           frontend
│           factuality
│           endedness
│           weren
│           doesn
│           isn
│           pre
│           reorganized
│           prioritize
├── favicon.png
│   ├── type: file
│   └── content
│       ├── file_name: favicon.png
│       ├── file_type: .png
│       ├── file_stats
│       │   ├── bytes: 4117
│       │   ├── last_modified_utc: 1698361445.802428
│       │   ├── last_accessed_utc: 1698361446.0213444
│       │   └── created_utc: 1698361445.802428
│       └── content: <content could not be loaded>
├── quality.rst
│   ├── type: file
│   └── content
│       ├── file_name: quality.rst
│       ├── file_type: .rst
│       ├── file_stats
│       │   ├── bytes: 11330
│       │   ├── last_modified_utc: 1698361445.8404584
│       │   ├── last_accessed_utc: 1698361446.6335802
│       │   └── created_utc: 1698361445.8404584
│       └── content: Towards a theory of quality in documentation
│           ===============================================
│           
│           Diátax
│           ...
│           taxis *can* do is lay down some conditions for the
│           *possibility* of deep quality in documentation.
│           
│           
├── complex-hierarchies.rst
│   ├── type: file
│   └── content
│       ├── file_name: complex-hierarchies.rst
│       ├── file_type: .rst
│       ├── file_stats
│       │   ├── bytes: 9030
│       │   ├── last_modified_utc: 1698361445.801645
│       │   ├── last_accessed_utc: 1698361445.9629655
│       │   └── created_utc: 1698361445.801645
│       └── content: .. _complex-documentation:
│           
│           Diátaxis in complex hierarchies
│           ==================================
│           
│           .. _
│           ...
│           rward to navigate as long as they are logical and incorporate
│           patterns that fit the needs of users.
│           
├── make.bat
│   ├── type: file
│   └── content
│       ├── file_name: make.bat
│       ├── file_type: .bat
│       ├── file_stats
│       │   ├── bytes: 760
│       │   ├── last_modified_utc: 1698361445.839894
│       │   ├── last_accessed_utc: 1698361445.9577377
│       │   └── created_utc: 1698361445.839894
│       └── content: @ECHO OFF
│           
│           pushd %~dp0
│           
│           REM Command file for Sphinx documentation
│           
│           if "%SPHINXBUILD%" == "" (
│                   set S
│           ...
│           XOPTS% %O%
│           goto end
│           
│           :help
│           %SPHINXBUILD% -M help %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%
│           
│           :end
│           popd
│           
├── .gitignore
│   ├── type: file
│   └── content
│       ├── file_name: .gitignore
│       ├── file_type: 
│       ├── file_stats
│       │   ├── bytes: 53
│       │   ├── last_modified_utc: 1698361445.7995565
│       │   ├── last_accessed_utc: 1698361482.3879392
│       │   └── created_utc: 1698361445.7995565
│       └── content: /*env*/
│           _build
│           .DS_Store
│           __pycache__
│           .idea/
│           stashed/
│           
├── LICENSE.rst
│   ├── type: file
│   └── content
│       ├── file_name: LICENSE.rst
│       ├── file_type: .rst
│       ├── file_stats
│       │   ├── bytes: 18846
│       │   ├── last_modified_utc: 1698361445.8000042
│       │   ├── last_accessed_utc: 1698361445.9704216
│       │   └── created_utc: 1698361445.8000042
│       └── content: Creative Commons Attribution-ShareAlike 4.0 International
│           ==========================================
│           ...
│            form part of the public licenses.``
│           
│           ``Creative Commons may be contacted at creativecommons.org.``
│           
├── diataxis.png
│   ├── type: file
│   └── content
│       ├── file_name: diataxis.png
│       ├── file_type: .png
│       ├── file_stats
│       │   ├── bytes: 25408
│       │   ├── last_modified_utc: 1698361445.8020048
│       │   ├── last_accessed_utc: 1698361445.9503005
│       │   └── created_utc: 1698361445.8020048
│       └── content: <content could not be loaded>
├── tutorials.rst
│   ├── type: file
│   └── content
│       ├── file_name: tutorials.rst
│       ├── file_type: .rst
│       ├── file_stats
│       │   ├── bytes: 13901
│       │   ├── last_modified_utc: 1698361445.841952
│       │   ├── last_accessed_utc: 1698361446.6681774
│       │   └── created_utc: 1698361445.841952
│       └── content: .. _tutorials:
│           
│           About tutorials
│           ===============
│           
│           ..  rubric:: Tutorials are **lessons** that take th
│           ...
│            (and admire, in a mild way) what your learner has accomplished 
│           (note - not: "you have learned...")
│           
├── README.rst
│   ├── type: file
│   └── content
│       ├── file_name: README.rst
│       ├── file_type: .rst
│       ├── file_stats
│       │   ├── bytes: 275
│       │   ├── last_modified_utc: 1698361445.800308
│       │   ├── last_accessed_utc: 1698361445.9608033
│       │   └── created_utc: 1698361445.800308
│       └── content: The documentation system
│           ========================
│           
│           A comprehensive and practical system that can hel
│           ...
│           Author: Daniele Procida
│           
│           License: `CC-BY-SA 4.0 
│           <https://creativecommons.org/licenses/by-sa/4.0/>`_
│           
├── tutorials-how-to.rst
│   ├── type: file
│   └── content
│       ├── file_name: tutorials-how-to.rst
│       ├── file_type: .rst
│       ├── file_stats
│       │   ├── bytes: 15425
│       │   ├── last_modified_utc: 1698361445.8416603
│       │   ├── last_accessed_utc: 1698361446.6714292
│       │   └── created_utc: 1698361445.8416603
│       └── content: .. _tutorials-how-to:
│           
│           What’s the difference between a tutorial and how-to guide?
│           ==================
│           ...
│           e sake of those users, and of our own
│           product, getting the distinction right is a key to success.
│           
│           
│           
├── reference-explanation.rst
│   ├── type: file
│   └── content
│       ├── file_name: reference-explanation.rst
│       ├── file_type: .rst
│       ├── file_stats
│       │   ├── bytes: 3578
│       │   ├── last_modified_utc: 1698361445.840704
│       │   ├── last_accessed_utc: 1698361446.651539
│       │   └── created_utc: 1698361445.840704
│       └── content: .. _reference-explanation:
│           
│           Explanation and reference
│           ==========================
│           
│           Explanation and re
│           ...
│           ps and responding to the needs in them is the key to creating
│           effective reference and explanation.
│           
│           
├── needs.rst
│   ├── type: file
│   └── content
│       ├── file_name: needs.rst
│       ├── file_type: .rst
│       ├── file_stats
│       │   ├── bytes: 7856
│       │   ├── last_modified_utc: 1698361445.84016
│       │   ├── last_accessed_utc: 1698361446.684549
│       │   └── created_utc: 1698361445.84016
│       └── content: .. _needs:
│           
│           The map of needs
│           =============================
│           
│           *How to organise my documentation?* In t
│           ...
│           le.
│           
│           And then it's back to the beginning, perhaps for a new thing to 
│           grasp, or to penetrate deeper.
│           
├── compass.rst
│   ├── type: file
│   └── content
│       ├── file_name: compass.rst
│       ├── file_type: .rst
│       ├── file_stats
│       │   ├── bytes: 1989
│       │   ├── last_modified_utc: 1698361445.801431
│       │   ├── last_accessed_utc: 1698361445.9489732
│       │   └── created_utc: 1698361445.801431
│       └── content: .. _compass:
│           
│           The compass
│           =======================
│           
│           The Diátaxis map is an effective reminder of the 
│           ...
│           es more effective and accurate
│           with practice, but it quickly becomes a useful decision-making tool.
│           
├── how-to-use-diataxis.rst
│   ├── type: file
│   └── content
│       ├── file_name: how-to-use-diataxis.rst
│       ├── file_type: .rst
│       ├── file_stats
│       │   ├── bytes: 7000
│       │   ├── last_modified_utc: 1698361445.802755
│       │   ├── last_accessed_utc: 1698361445.9727082
│       │   └── created_utc: 1698361445.802755
│       └── content: .. _how-to-use-diataxis:
│           
│           How to use Diátaxis
│           ===================
│           
│           In short, the answer is: **pragma
│           ...
│           rent stage of development, and in a healthy
│           structural state and ready to go on to the next stage.
│           
│           
├── .readthedocs.yaml
│   ├── type: file
│   └── content
│       ├── file_name: .readthedocs.yaml
│       ├── file_type: .yaml
│       ├── file_stats
│       │   ├── bytes: 582
│       │   ├── last_modified_utc: 1698361445.799696
│       │   ├── last_accessed_utc: 1698361482.348955
│       │   └── created_utc: 1698361445.799696
│       └── content: # .readthedocs.yaml
│           # Read the Docs configuration file
│           # See https://docs.readthedocs.io/en/stable/c
│           ...
│           .io/en/stable/guides/reproducible-builds.html
│           python:
│             install:
│             - requirements: requirements.txt
│           
├── images/
│   ├── suture.jpg
│   │   ├── type: file
│   │   └── content
│   │       ├── file_name: suture.jpg
│   │       ├── file_type: .jpg
│   │       ├── file_stats
│   │       │   ├── bytes: 104514
│   │       │   ├── last_modified_utc: 1698361445.838013
│   │       │   ├── last_accessed_utc: 1698361779.5234268
│   │       │   └── created_utc: 1698361445.838013
│   │       └── content: <content could not be loaded>
│   ├── always-complete.jpg
│   │   ├── type: file
│   │   └── content
│   │       ├── file_name: always-complete.jpg
│   │       ├── file_type: .jpg
│   │       ├── file_stats
│   │       │   ├── bytes: 1081847
│   │       │   ├── last_modified_utc: 1698361445.8075411
│   │       │   ├── last_accessed_utc: 1698361779.5143473
│   │       │   └── created_utc: 1698361445.8075411
│   │       └── content: <content could not be loaded>
│   ├── collapse.png
│   │   ├── type: file
│   │   └── content
│   │       ├── file_name: collapse.png
│   │       ├── file_type: .png
│   │       ├── file_stats
│   │       │   ├── bytes: 224248
│   │       │   ├── last_modified_utc: 1698361445.8107224
│   │       │   ├── last_accessed_utc: 1698361779.51666
│   │       │   └── created_utc: 1698361445.8107224
│   │       └── content: <content could not be loaded>
│   ├── django-tutorial-example.png
│   │   ├── type: file
│   │   └── content
│   │       ├── file_name: django-tutorial-example.png
│   │       ├── file_type: .png
│   │       ├── file_stats
│   │       │   ├── bytes: 102306
│   │       │   ├── last_modified_utc: 1698361445.8190382
│   │       │   ├── last_accessed_utc: 1698361779.5183241
│   │       │   └── created_utc: 1698361445.8190382
│   │       └── content: <content could not be loaded>
│   ├── old-recipe.jpg
│   │   ├── type: file
│   │   └── content
│   │       ├── file_name: old-recipe.jpg
│   │       ├── file_type: .jpg
│   │       ├── file_stats
│   │       │   ├── bytes: 316167
│   │       │   ├── last_modified_utc: 1698361445.8293073
│   │       │   ├── last_accessed_utc: 1698361779.5209432
│   │       │   └── created_utc: 1698361445.8293073
│   │       └── content: <content could not be loaded>
│   ├── diataxis-white-416.png
│   │   ├── type: file
│   │   └── content
│   │       ├── file_name: diataxis-white-416.png
│   │       ├── file_type: .png
│   │       ├── file_stats
│   │       │   ├── bytes: 14872
│   │       │   ├── last_modified_utc: 1698361445.8117561
│   │       │   ├── last_accessed_utc: 1698361445.9564447
│   │       │   └── created_utc: 1698361445.8117561
│   │       └── content: <content could not be loaded>
│   ├── django-how-to-example.png
│   │   ├── type: file
│   │   └── content
│   │       ├── file_name: django-how-to-example.png
│   │       ├── file_type: .png
│   │       ├── file_stats
│   │       │   ├── bytes: 178399
│   │       │   ├── last_modified_utc: 1698361445.817002
│   │       │   ├── last_accessed_utc: 1698361779.5177765
│   │       │   └── created_utc: 1698361445.817002
│   │       └── content: <content could not be loaded>
│   ├── overview-reference.png
│   │   ├── type: file
│   │   └── content
│   │       ├── file_name: overview-reference.png
│   │       ├── file_type: .png
│   │       ├── file_stats
│   │       │   ├── bytes: 48636
│   │       │   ├── last_modified_utc: 1698361445.8335989
│   │       │   ├── last_accessed_utc: 1698361779.522353
│   │       │   └── created_utc: 1698361445.8335989
│   │       └── content: <content could not be loaded>
│   ├── total-collapse.png
│   │   ├── type: file
│   │   └── content
│   │       ├── file_name: total-collapse.png
│   │       ├── file_type: .png
│   │       ├── file_stats
│   │       │   ├── bytes: 139903
│   │       │   ├── last_modified_utc: 1698361445.83927
│   │       │   ├── last_accessed_utc: 1698361779.523611
│   │       │   └── created_utc: 1698361445.83927
│   │       └── content: <content could not be loaded>
│   ├── overview.png
│   │   ├── type: file
│   │   └── content
│   │       ├── file_name: overview.png
│   │       ├── file_type: .png
│   │       ├── file_stats
│   │       │   ├── bytes: 209013
│   │       │   ├── last_modified_utc: 1698361445.8350787
│   │       │   ├── last_accessed_utc: 1698361779.5225458
│   │       │   └── created_utc: 1698361445.8350787
│   │       └── content: <content could not be loaded>
│   ├── ginger.jpg
│   │   ├── type: file
│   │   └── content
│   │       ├── file_name: ginger.jpg
│   │       ├── file_type: .jpg
│   │       ├── file_stats
│   │       │   ├── bytes: 235835
│   │       │   ├── last_modified_utc: 1698361445.8208916
│   │       │   ├── last_accessed_utc: 1698361779.5185003
│   │       │   └── created_utc: 1698361445.8208916
│   │       └── content: <content could not be loaded>
│   ├── overview-how-to.png
│   │   ├── type: file
│   │   └── content
│   │       ├── file_name: overview-how-to.png
│   │       ├── file_type: .png
│   │       ├── file_stats
│   │       │   ├── bytes: 44451
│   │       │   ├── last_modified_utc: 1698361445.8331034
│   │       │   ├── last_accessed_utc: 1698361779.52224
│   │       │   └── created_utc: 1698361445.8331034
│   │       └── content: <content could not be loaded>
│   ├── diataxis-white-original.png
│   │   ├── type: file
│   │   └── content
│   │       ├── file_name: diataxis-white-original.png
│   │       ├── file_type: .png
│   │       ├── file_stats
│   │       │   ├── bytes: 63583
│   │       │   ├── last_modified_utc: 1698361445.8122241
│   │       │   ├── last_accessed_utc: 1698361779.5170617
│   │       │   └── created_utc: 1698361445.8122241
│   │       └── content: <content could not be loaded>
│   ├── divio-explanation-example.png
│   │   ├── type: file
│   │   └── content
│   │       ├── file_name: divio-explanation-example.png
│   │       ├── file_type: .png
│   │       ├── file_stats
│   │       │   ├── bytes: 142553
│   │       │   ├── last_modified_utc: 1698361445.8159208
│   │       │   ├── last_accessed_utc: 1698361779.517539
│   │       │   └── created_utc: 1698361445.8159208
│   │       └── content: <content could not be loaded>
│   ├── anselmo.jpg
│   │   ├── type: file
│   │   └── content
│   │       ├── file_name: anselmo.jpg
│   │       ├── file_type: .jpg
│   │       ├── file_stats
│   │       │   ├── bytes: 428662
│   │       │   ├── last_modified_utc: 1698361445.809365
│   │       │   ├── last_accessed_utc: 1698361779.5159907
│   │       │   └── created_utc: 1698361445.809365
│   │       └── content: <content could not be loaded>
│   ├── overview-explanation.png
│   │   ├── type: file
│   │   └── content
│   │       ├── file_name: overview-explanation.png
│   │       ├── file_type: .png
│   │       ├── file_stats
│   │       │   ├── bytes: 55466
│   │       │   ├── last_modified_utc: 1698361445.8325298
│   │       │   ├── last_accessed_utc: 1698361779.5220964
│   │       │   └── created_utc: 1698361445.8325298
│   │       └── content: <content could not be loaded>
│   ├── partial-collapse.png
│   │   ├── type: file
│   │   └── content
│   │       ├── file_name: partial-collapse.png
│   │       ├── file_type: .png
│   │       ├── file_stats
│   │       │   ├── bytes: 129799
│   │       │   ├── last_modified_utc: 1698361445.8359404
│   │       │   ├── last_accessed_utc: 1698361779.5228791
│   │       │   └── created_utc: 1698361445.8359404
│   │       └── content: <content could not be loaded>
│   ├── diataxis.png
│   │   ├── type: file
│   │   └── content
│   │       ├── file_name: diataxis.png
│   │       ├── file_type: .png
│   │       ├── file_stats
│   │       │   ├── bytes: 156896
│   │       │   ├── last_modified_utc: 1698361445.814998
│   │       │   ├── last_accessed_utc: 1698361779.5172822
│   │       │   └── created_utc: 1698361445.814998
│   │       └── content: <content could not be loaded>
│   ├── operation.jpg
│   │   ├── type: file
│   │   └── content
│   │       ├── file_name: operation.jpg
│   │       ├── file_type: .jpg
│   │       ├── file_stats
│   │       │   ├── bytes: 264617
│   │       │   ├── last_modified_utc: 1698361445.83172
│   │       │   ├── last_accessed_utc: 1698361779.5216134
│   │       │   └── created_utc: 1698361445.83172
│   │       └── content: <content could not be loaded>
│   ├── overview-tutorials.png
│   │   ├── type: file
│   │   └── content
│   │       ├── file_name: overview-tutorials.png
│   │       ├── file_type: .png
│   │       ├── file_stats
│   │       │   ├── bytes: 42443
│   │       │   ├── last_modified_utc: 1698361445.8340442
│   │       │   ├── last_accessed_utc: 1698361779.5224557
│   │       │   └── created_utc: 1698361445.8340442
│   │       └── content: <content could not be loaded>
│   ├── mcgee.jpg
│   │   ├── type: file
│   │   └── content
│   │       ├── file_name: mcgee.jpg
│   │       ├── file_type: .jpg
│   │       ├── file_stats
│   │       │   ├── bytes: 152303
│   │       │   ├── last_modified_utc: 1698361445.828063
│   │       │   ├── last_accessed_utc: 1698361779.5206847
│   │       │   └── created_utc: 1698361445.828063
│   │       └── content: <content could not be loaded>
│   ├── recipe.jpg
│   │   ├── type: file
│   │   └── content
│   │       ├── file_name: recipe.jpg
│   │       ├── file_type: .jpg
│   │       ├── file_stats
│   │       │   ├── bytes: 208426
│   │       │   ├── last_modified_utc: 1698361445.83712
│   │       │   ├── last_accessed_utc: 1698361779.5230954
│   │       │   └── created_utc: 1698361445.83712
│   │       └── content: <content could not be loaded>
│   ├── liquorice.png
│   │   ├── type: file
│   │   └── content
│   │       ├── file_name: liquorice.png
│   │       ├── file_type: .png
│   │       ├── file_stats
│   │       │   ├── bytes: 1189299
│   │       │   ├── last_modified_utc: 1698361445.8267577
│   │       │   ├── last_accessed_utc: 1698361779.5188723
│   │       │   └── created_utc: 1698361445.8267577
│   │       └── content: <content could not be loaded>
│   ├── diataxis-white.png
│   │   ├── type: file
│   │   └── content
│   │       ├── file_name: diataxis-white.png
│   │       ├── file_type: .png
│   │       ├── file_stats
│   │       │   ├── bytes: 47911
│   │       │   ├── last_modified_utc: 1698361445.8129585
│   │       │   ├── last_accessed_utc: 1698361779.5171845
│   │       │   └── created_utc: 1698361445.8129585
│   │       └── content: <content could not be loaded>
│   └── django-reference-example.png
│       ├── type: file
│       └── content
│           ├── file_name: django-reference-example.png
│           ├── file_type: .png
│           ├── file_stats
│           │   ├── bytes: 146194
│           │   ├── last_modified_utc: 1698361445.8179808
│           │   ├── last_accessed_utc: 1698361779.5180788
│           │   └── created_utc: 1698361445.8179808
│           └── content: <content could not be loaded>
├── _templates/
│   ├── page.html
│   │   ├── type: file
│   │   └── content
│   │       ├── file_name: page.html
│   │       ├── file_type: .html
│   │       ├── file_stats
│   │       │   ├── bytes: 1624
│   │       │   ├── last_modified_utc: 1698361445.8006942
│   │       │   ├── last_accessed_utc: 1698361482.2590861
│   │       │   └── created_utc: 1698361445.8006942
│   │       └── content: {% extends "furo/page.html" %}
│   │           
│   │             {% block site_meta %}
│   │             <meta name="author" content="Daniele Proci
│   │           ...
│   │           io-and-diataxis">Divio</a>.
│   │                 {%- endtrans %}
│   │               {%- endif %}
│   │             </div>
│   │             {% endblock footer %}
│   │           
│   └── sidebar/
│       └── contact.html
│           ├── type: file
│           └── content
│               ├── file_name: contact.html
│               ├── file_type: .html
│               ├── file_stats
│               │   ├── bytes: 757
│               │   ├── last_modified_utc: 1698361445.8008733
│               │   ├── last_accessed_utc: 1698361482.2596078
│               │   └── created_utc: 1698361445.8008733
│               └── content: <div class="sidebar-contact">
│                     <h2>{{ _("Contact") }}</h2>
│                   
│                     <div>
│                       <ul>
│                       <li><p><a class="r
│                   ...
│                   f="https://www.writethedocs.org/slack/">Write the Docs 
│                   Slack</a></p></li>
│                       </ul>
│                     </div>
│                   
│                   </div>
└── _static/
    └── diataxis.css
        ├── type: file
        └── content
            ├── file_name: diataxis.css
            ├── file_type: .css
            ├── file_stats
            │   ├── bytes: 4780
            │   ├── last_modified_utc: 1698361445.8005106
            │   ├── last_accessed_utc: 1698361445.961934
            │   └── created_utc: 1698361445.8005106
            └── content: @import 
                url('https://fonts.googleapis.com/css2?family=Source+Sans+Pro:it
                al@0;1&family=Source+Serif+P
                ...
                :last-child th {border-bottom: none;}
                table.docutils thead {border-bottom: 1px solid var(--orange);}


```

