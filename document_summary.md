+++++++++++++++++++++++++++++++++++

FILE_PATH - diataxis-documentation-framework-repo/colofon.rst
STATUS - Almost done
## Colofon
### Origins and development
The Diátaxis documentation framework was originally developed for software product documentation and has since been applied in various contexts such as internal corporate documentation, scientific research, organizational management, and education.
### Divio and Diátaxis
The key concepts of Diátaxis were developed while working at Divio, a cloud applications platform. The ideas were presented at conferences in 2017 and later documented as "The documentation system for Divio." The Diátaxis documentation philosophy is based on the thinking and approaches developed at Divio.
### Contact the author
Readers can contact the author, Daniele Procida, via email or through the Write the Docs Slack group or GitHub repository.
### How to cite Diátaxis
Instructions for citing Diátaxis are provided on the website, including a citation file in the Git repository and APA and BibTeX metadata.
### Website
The Diátaxis website is built with Sphinx and hosted on Read the Docs, using a modified version of the Furo theme by Pradyun Gedam.

-----------------------------------

+++++++++++++++++++++++++++++++++++

FILE_PATH - diataxis-documentation-framework-repo/adoption.rst
STATUS - In progress

## Who's using Diátaxis?
### Testimonials
- Gatsby recently reorganized their open-source documentation using the Diátaxis framework, which helped prioritize user goals and make resources more easily discoverable.

### Adoption List
- Aiven Developer: developer documentation for managed open source data platforms
- BBC News Labs: documentation for various projects, including mosromgr
- BrachioGraph: documentation for the pen-plotter
- BeeWare: documentation for Toga, Briefcase, Rubicon, and Rubicon Java
- Bosch (internal)
- Canonical: all of Canonical's product documentation is adopting or will adopt Diátaxis
- Ciw: documentation for the discrete event simulation library
- clj-otel: Clojure API for OpenTelemetry
- Cloudflare Workers docs: documentation for Cloudflare Workers
- corrux (internal)
- Divio
- Django
- django CMS
- edo: documentation for the library for Evolutionary Dataset Optimisation
- Encore: documentation for the framework for rapid backend development
- Ericsson (internal)
- fpm: documentation for the Fortran Package Manager
- Google's Fuchsia operating system
- Funding Circle (internal)
- Gatsby
- Gensim: documentation for the Gensim library
- Gorgonia: documentation for the deep learning library for Go
- gtk-fortran: documentation for the Fortran bindings for GTK
- ING Bank: documentation for open-source and internal tooling projects
- Lisk
- Livepeer
- LootLocker: documentation for the backend for independent games development
- Matching: documentation for the games theory resource allocation library
- NashPy: documentation for the Python mathematical library for computing Nash equilibria
- nbchkr: documentation for the system for assessing students' assignments in Jupyter Notebooks
- NumPy: documentation for the scientific Python library
- PDFminer.six
- PostgREST
- PowerTuning (internal)
- PIconnect
- Snowpack: documentation for the frontend build tool
- Sourcegraph: documentation for Universal code search
- Splink: documentation for the Python library for probabilistic data linkage
- stdlib: documentation for the Fortran Standard library
- StrongLoop/LoopBack by IBM
- TerminusDB
- Tesla Motors (internal)
- WebAccess/DMP
- websockets
- Wechaty: documentation for the Conversational RPA SDK for Chatbot Makers
- Zalando (internal)

## Other mentions and references of interest
- Django Axes proposal
- GitLab: GitLab's Data Team documentation guide
- Julia language proposal
- Why You Should Document Your Work As a Data Scientist
- Koninglijke Biblioteek (National Library of the Netherlands) research software lab
- Tutorials in Jenkins user documentation
- TYPO3

-----------------------------------

+++++++++++++++++++++++++++++++++++

FILE_PATH - diataxis-documentation-framework-repo/index.rst
STATUS - In progress

## Diátaxis
### A systematic approach to technical documentation authoring.

The Diátaxis framework aims to solve the problem of quality in technical documentation by providing an information architecture that makes it easier to create, maintain, and use. It identifies four modes of documentation - tutorials, how-to guides, technical reference, and explanation - and structures documentation explicitly around these four types. Each type fulfills a different purpose and requires a different approach to its creation. The framework is proven in practice across various fields and applications and is light-weight, easy to understand, and straightforward to apply. It does not impose implementation constraints and helps make projects and teams more successful.

-----------------------------------

+++++++++++++++++++++++++++++++++++

FILE_PATH - diataxis-documentation-framework-repo/explanation.rst
STATUS - In progress
## About explanation
   ### Explanation clarifies, deepens and broadens the reader’s understanding of a subject.
   ### The value and place of explanation
      #### Explanation and understanding
         - Explanation is important for practitioners to have a comprehensive understanding of their craft.
      #### Explanation and its boundaries
         - Explanation is often scattered throughout documentation rather than having its own section.
## Analogy from cooking
   - The book "On food and cooking" by Harold McGee is an example of explanation that changes how we think about cooking.
## Writing good explanation
   ### Make connections
      - Make connections to other topics to help readers understand.
   ### Provide context
      - Provide background and context to explain why things are the way they are.
   ### Talk *about* the subject
      - Explanation guides should be about a topic and provide a higher-level understanding.
   ### Discuss alternatives and opinions
      - Explanation can consider alternatives and multiple approaches to a question.
   ### Don't instruct, or provide technical reference
      - Explanation should not provide instructions or technical descriptions.
## The language of explanation
   - The language of explanation includes providing explanations, offering judgments and opinions, providing context, weighing up alternatives, and unfolding the internal secrets of a system.

-----------------------------------

+++++++++++++++++++++++++++++++++++

FILE_PATH - diataxis-documentation-framework-repo/reference.rst
STATUS - In progress
## About reference
### Reference as description
### Food and cooking
### Writing a good reference guide
#### Respect the structure of the machinery
#### Be consistent
#### Do nothing but describe
#### Provide examples
#### Be accurate
## The language of reference guides


-----------------------------------

+++++++++++++++++++++++++++++++++++

FILE_PATH - diataxis-documentation-framework-repo/how-to-guides.rst
STATUS - In progress

## About how-to guides
### How-to guides are directions that take the reader through the steps required to solve a real-world problem. They are goal-oriented and can be thought of as recipes for achieving a specific end. Examples include calibrating a radar array or configuring reconnection back-off policies. How-to guides are distinct from tutorials and serve different user needs.

## Tutorials vs how-to guides
### How-to guides and tutorials are often confused, but they serve different purposes. How-to guides provide practical steps to complete a task, while tutorials provide a comprehensive guide from start to finish. Conflating the two can lead to difficulties in documentation.

## Food and cooking
### A recipe is an excellent model for a how-to guide. It clearly defines what will be achieved and addresses a specific question. A recipe does not teach how to make something but provides a sequence of actions to follow. Following a recipe requires basic competence and is not a substitute for a cooking lesson.

## Writing a good how-to guide
### A good how-to guide describes a sequence of actions in a specific order. It focuses on tasks or problems, assumes the user knows what they want to achieve, and provides only action without digression or explanation. It should solve a problem and not try to explain concepts. A how-to guide should be flexible and adaptable to real-world use-cases. Practical usability is more important than completeness, and attention should be paid to naming. Good titles should accurately reflect what the guide shows.

## The language of how-to guides
### How-to guides should use clear language to describe the problem or task they solve. Conditional imperatives should be used, and unnecessary information should be omitted. References to other guides can be provided for additional information.

-----------------------------------

+++++++++++++++++++++++++++++++++++

FILE_PATH - diataxis-documentation-framework-repo/quality.rst
STATUS - In progress

## Towards a theory of quality in documentation
### Diátaxis is an approach to quality in documentation that distinguishes between functional quality and deep quality.
- Functional quality refers to meeting standards of accuracy, completeness, consistency, usefulness, and precision.
- Deep quality refers to characteristics such as feeling good to use, having flow, fitting to human needs, being beautiful, and anticipating the user.
- Functional quality can be objectively measured, while deep quality is subjective and can only be assessed in light of human needs.
- Deep quality is conditional upon functional quality, and documentation can meet functional quality standards without exhibiting deep quality.
- Characteristics of functional quality are independent of each other, while characteristics of deep quality are interdependent.
- Functional quality represents constraints, while deep quality represents liberation and creativity.

### How we recognize deep quality
- Deep quality in documentation can be recognized by the pleasure and satisfaction experienced when using it.
- Users may not be able to articulate why documentation is good, but they can still recognize its excellence based on how it feels to use.
- Documentation creators need a clear understanding of what makes documentation good and how users will feel when using it.

### Diátaxis and quality
- Diátaxis cannot address functional quality in documentation but can expose lapses in functional quality.
- Diátaxis can contribute to deep quality by helping documentation fit user needs and preserving flow.
- Diátaxis offers principles for achieving deep quality but does not guarantee it.
- Diátaxis lays down conditions for the possibility of deep quality in documentation.

-----------------------------------

+++++++++++++++++++++++++++++++++++

FILE_PATH - diataxis-documentation-framework-repo/complex-hierarchies.rst
STATUS - In progress

## Diátaxis in complex hierarchies
### The basics
- Diátaxis can be applied to most documentation with clear boundaries and a simple arrangement of contents.
- The structure includes landing pages for each section, providing an overview of the contents within.
### Adding a layer of hierarchy
- Large documentation sets can benefit from an additional layer of hierarchy to group pages within sections.
- Each level of the hierarchy has an overview landing page for orientation.
### The problem of lists
- Lists longer than a few items are difficult to read, so breaking them up into smaller ones is necessary.
- The focus should be on the reader's experience and finding a way to make the content more manageable.
### Overviews and introductory text
- Landing pages should read like overviews, introducing the content rather than simply presenting lists.
- Headings and snippets of introductory text provide context and catch the reader's attention.
### Two-dimensional problems
- When Diátaxis meets another structure or different user types, a more complex hierarchy may be needed.
- Examples include a product used on land, sea, and air, or documentation for users, developers, and contributors.
- The structure should be based on user needs and may involve repetition or shared material.
### What *is* the problem?
- The problem is not limited to Diátaxis but is revealed and brought into focus by its application.
- Diátaxis is an approach, not a rigid scheme, that identifies four different needs for effective documentation.
### Diátaxis as an approach
- Diátaxis is a way of working with documentation that structures it based on four different needs.
- The outcome is typically a clear division into the four categories, but that is not the end goal.
### User-first thinking
- Diátaxis is driven by attention to user needs and the product as it is for the user.
- The structure should reflect how users perceive the product, even if it is complex or requires different perspectives.
### Let documentation be complex if necessary
- Documentation should be as complex as needed, but it should still be logical and incorporate patterns that meet user needs.

-----------------------------------

+++++++++++++++++++++++++++++++++++

FILE_PATH - diataxis-documentation-framework-repo/LICENSE.rst
STATUS - In progress
## Creative Commons Public Licenses
### Using Creative Commons Public Licenses
- Creative Commons licenses provide terms and conditions for sharing original works of authorship and other material subject to copyright and certain other rights.
- Licensors should read and understand the terms and conditions of the license they choose before applying it.
- Licensors should secure all necessary rights before applying the license.
- Licensors should clearly mark any material not subject to the license.
- Users of the licensed material should respect any special requests made by the licensor.
### Creative Commons Attribution-ShareAlike 4.0 International Public License
- By exercising the Licensed Rights, the user accepts and agrees to be bound by the terms and conditions of this license.
- The license grants the user the right to reproduce, share, and produce adapted material.
- The license does not apply if there are exceptions and limitations to the user's use.
- The license allows technical modifications necessary to exercise the Licensed Rights.
- Downstream recipients automatically receive an offer to exercise the Licensed Rights.
- No additional or different terms or conditions can be imposed on the Licensed Material.
### License Conditions
- Attribution: If the user shares the Licensed Material, they must retain certain information and indicate any modifications made.
- ShareAlike: If the user shares Adapted Material, they must apply a compatible license and include the text or link to the Adapter's License.
### Sui Generis Database Rights
- If the Licensed Rights include Sui Generis Database Rights, the user has the right to extract, reuse, reproduce, and share the contents of the database.
- If the user includes the database contents in a database with Sui Generis Database Rights, the database is considered Adapted Material.
### Disclaimer of Warranties and Limitation of Liability
- The Licensor offers the Licensed Material as-is and makes no warranties.
- The Licensor is not liable for any losses, costs, expenses, or damages arising from the use of the Licensed Material.
### Term and Termination
- The Public License applies for the term of the Copyright and Similar Rights.
- Violations of the Public License automatically terminate the user's rights.
- The Licensor may reinstate the user's rights upon cure of the violation.
- The Licensor may offer the Licensed Material under separate terms or conditions or stop distributing it at any time.
### Other Terms and Conditions
- The Licensor is not bound by any additional or different terms or conditions communicated by the user.
### Interpretation
- The Public License does not reduce or limit any use of the Licensed Material that could be made without permission.
- Unenforceable provisions of the Public License will be reformed or severed.
- No waiver or failure to comply is allowed unless expressly agreed.
- The use of the trademark "Creative Commons" requires prior written consent.

-----------------------------------

+++++++++++++++++++++++++++++++++++

FILE_PATH - diataxis-documentation-framework-repo/tutorials.rst
STATUS - In progress

## About tutorials
### Tutorials are lessons that guide the reader through a series of steps to complete a project. They are learning-oriented and aim to help beginners achieve basic competence with a product.

## The tutorial as a lesson
### A lesson is a learning experience where learning takes place through what the pupil does. The teacher has the responsibility to guide the pupil's learning and ensure the lesson is meaningful, successful, logical, and complete.

## The problem of tutorials
### Tutorials are often the weakest part of documentation and are difficult to create and maintain. They require a significant amount of work and are subject to frequent revisions. Inadequate tutorials can prevent a project from acquiring new users.

## Food and cooking
### Teaching a child to cook demonstrates the main demands imposed by a tutorial. The important thing is for the child to enjoy the experience, gain confidence, and want to do it again. The child learns through repetition and practical knowledge.

## Writing a good tutorial
### A good tutorial allows the user to learn by doing. It gets the user started, provides a complete picture before they start, works reliably, shows immediate results, is repeatable, describes concrete steps, offers only necessary explanations, and ignores options and alternatives.

## The language of tutorials
### The language of tutorials should describe what the learner will accomplish, provide clear instructions, minimal explanations, clear expectations, clues for confirmation, and descriptions of what the learner has accomplished.

-----------------------------------

+++++++++++++++++++++++++++++++++++

FILE_PATH - diataxis-documentation-framework-repo/README.rst
STATUS - In progress

## The documentation system
### A comprehensive and practical system that can help maintainers of product documentation.
#### Published at https://diataxis.fr
#### Author: Daniele Procida
#### License: CC-BY-SA 4.0

## Notes:
- Strengths
    - Comprehensive and practical system
    - Helps maintainers of product documentation
- Weaknesses
    - None mentioned in the text

-----------------------------------

+++++++++++++++++++++++++++++++++++

FILE_PATH - diataxis-documentation-framework-repo/tutorials-how-to.rst
STATUS - In progress
## What’s the difference between a tutorial and how-to guide?
### What they have in common
- Tutorials and how-to guides are both practical guides that provide directions for the user to follow.
- They both describe ordered sequences of actions and promise a successful outcome if followed correctly.
### What matters is what the user needs
- Tutorials serve the needs of users who are studying and aim to provide a successful learning experience.
- How-to guides serve the needs of users who are working and aim to help them accomplish a task.
### At study and at work
- Tutorials are lessons that familiarize learners with the work and provide a structured, repeatable encounter.
- How-to guides apply to the real world and assume familiarity with the tools, language, and processes.
### Understanding the distinction
- Tutorials focus on helping the learner acquire basic competence, while how-to guides help already-competent users perform a specific task correctly.
- Tutorials follow a carefully-managed path, while how-to guides guide the user along the safest, surest way to the goal.
- Tutorials eliminate the unexpected, while how-to guides prepare for the unexpected.
- Tutorials do not offer choices or alternatives, while how-to guides may describe different routes to the same destination.
- Tutorials must be safe, while how-to guides cannot promise safety.
- Responsibility lies with the teacher in tutorials, while the user has responsibility in how-to guides.
- Tutorials teach explicit basic things, while how-to guides rely on implicit knowledge.
- Tutorials are concrete and particular, while how-to guides take a general approach.
- Tutorials teach general skills and principles, while how-to guides focus on completing a particular task.
### The basic and the advanced
- Tutorials can cover basic procedures, and how-to guides can cover complex or advanced topics.
- The distinction between tutorials and how-to guides lies in the user's study or work needs.
### Safety and success
- Understanding the distinction between tutorials and how-to guides is crucial for creating successful documentation.
- Conflating education with practice in documentation can lead to harmful consequences and dissatisfaction among users.
- Getting the distinction right is key to success in attracting and retaining users.

-----------------------------------

+++++++++++++++++++++++++++++++++++

FILE_PATH - diataxis-documentation-framework-repo/reference-explanation.rst
STATUS - In progress
## Explanation and reference
### A straightforward distinction, *mostly*
- Reference and explanation belong to the theory half of the Diátaxis map
- Reference contains theoretical knowledge for application, while explanation is for acquiring knowledge and skill
- It is usually easy to recognize whether something is reference or explanation
- Boring and unmemorable content is likely reference, while content that can be read for enjoyment is likely explanation
- Asking a friend for more information about a topic would likely result in an explanation
### ... but intuition isn't reliable enough
- While intuition can usually be relied upon, it is easy to slip between reference and explanation
- Writing expansive reference material can lead to the inclusion of explanatory material, which is detrimental to both reference and explanation
### Work and study
- The distinction between reference and explanation can be determined by whether the content is used while working or for thinking about the topic
- Reference is used for applying knowledge and skill while working, while explanation is used for acquiring knowledge and skill through study
- Understanding these relationships is key to creating effective reference and explanation.

-----------------------------------

+++++++++++++++++++++++++++++++++++

FILE_PATH - diataxis-documentation-framework-repo/needs.rst
STATUS - In progress
## The map of needs
### How to organise my documentation?
- Documentation creators often struggle to structure their work around characteristics or features of the product it serves.
- Adopting a scheme that organizes documentation into clear content categories can improve it.
- Authors may find it difficult to fit their content within the categories of a scheme or may question the structure's arbitrariness.

## The Diátaxis map
### Description of the map
- The Diátaxis map is a two-dimensional structure that guides the organization of documentation.
- It places different forms of documentation in relationship with each other, highlighting their distinctions.
- The map is a map of needs, resulting in better and easier-to-create documentation.

## Needs
- Diátaxis is underpinned by a systematic description and analysis of generalized user needs.
- The user whose needs Diátaxis serves is the practitioner in a domain of skill.
- Documentation must meet the needs of theory and practical application, as well as the needs of study and work.

## Axes of knowledge
- Diátaxis divides documentation across two axes of knowledge: theory/practice and acquisition/application.
- Documentation contains either theoretical knowledge or describes practical actions.
- Documentation serves either the acquisition or application of knowledge.

## Characteristics of documentation
- Organizing material using Diátaxis provides clear expectations and guidance for both readers and authors.
- Different forms of documentation have specific purposes, writing styles, and placements.
- Documentation functions include tutorials, how-to guides, reference, and explanation.

## Collapse of the structure
- There is a natural tendency for the distinctions between different forms of documentation to blur.
- This can lead to structural problems, such as the collapse of tutorials and how-to guides into each other.

## The cycle of interaction
- Diátaxis aims to help documentation serve users in their cycle of interaction with a product.
- The cycle includes learning, task-oriented work, consulting technical reference, and reflecting on practice and knowledge.

-----------------------------------

+++++++++++++++++++++++++++++++++++

FILE_PATH - diataxis-documentation-framework-repo/compass.rst
STATUS - In progress
## The compass
### Introduction
The Diátaxis map is a helpful tool for understanding different types of documentation and their relationships. However, intuition alone is not always reliable when determining the appropriate form of documentation. The Diátaxis compass serves as a decision-making tool to guide authors in choosing the right type of documentation.
### The Diátaxis compass
The Diátaxis compass is similar to a truth-table or decision-tree for documentation. It simplifies the problem of choosing the appropriate documentation type and provides authors with a tool for course-correction.
### Documentation categories
The compass categorizes documentation based on the content and its purpose for the user. It provides four categories: practical steps for study, practical steps for work, theoretical knowledge for work, and theoretical knowledge for study.
### Application of the compass
The compass can be used to determine the appropriate documentation type for different user situations or to evaluate and improve existing documentation. It requires asking two questions: whether the documentation involves practical steps or theoretical knowledge, and whether it is for study or work. The compass becomes more effective with practice and serves as a valuable decision-making tool.

-----------------------------------

+++++++++++++++++++++++++++++++++++

FILE_PATH - diataxis-documentation-framework-repo/how-to-use-diataxis.rst
STATUS - In progress
## How to use Diátaxis
### Use Diátaxis as a guide, not a plan
### Don't worry about structure
### Work one step at a time
### Just do something
### Allow your work to develop organically

-----------------------------------

=============================================================

=============================================================

___ 
 > Global Summary 
  Here are the main points of the NIH R01 Proposal draft:

Specific Aims:
- The draft does not contain a Specific Aims section.

Research Strategy:

Significance:
- The draft does not have a Significance section.

Innovation:  
- The draft does not have an Innovation section.

Approach:
- The draft does not have an Approach section.

Aim 1: 
- The draft does not contain any aims.

Aim 2:
- The draft does not contain any aims.

Strengths:
- The draft text provides some background context about the Diátaxis documentation framework.

Weaknesses:
- The draft lacks all of the standard sections of an NIH R01 proposal, including Specific Aims, Research Strategy (Significance, Innovation, Approach), and specific Aims with experiments/methods. More background, rationale, preliminary data, and experimental detail needs to be added to turn this into a complete R01 proposal.

```

🌱
├── colofon.rst
│   ├── type: file
│   └── content
│       ├── file_name: colofon.rst
│       ├── file_type: .rst
│       ├── file_stats
│       │   ├── bytes: 3265
│       │   ├── last_modified_utc: 1696351005.0
│       │   ├── last_accessed_utc: 1698281240.661463
│       │   └── created_utc: 1698281219.0530398
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
│       │   ├── last_modified_utc: 1696351005.0
│       │   ├── last_accessed_utc: 1698281240.6680264
│       │   └── created_utc: 1698281219.0530686
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
│       │   ├── last_modified_utc: 1696351005.0
│       │   ├── last_accessed_utc: 1698281240.6645994
│       │   └── created_utc: 1698281219.0531034
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
│       │   ├── last_modified_utc: 1696351005.0
│       │   ├── last_accessed_utc: 1698281240.6569633
│       │   └── created_utc: 1698281219.0531342
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
│       │   ├── last_modified_utc: 1696351005.0
│       │   ├── last_accessed_utc: 1698281240.671635
│       │   └── created_utc: 1698281219.053166
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
│       │   ├── last_modified_utc: 1696351005.0
│       │   ├── last_accessed_utc: 1698281241.3690884
│       │   └── created_utc: 1698281219.0540354
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
│       │   ├── last_modified_utc: 1696351005.0
│       │   ├── last_accessed_utc: 1698281241.3601985
│       │   └── created_utc: 1698281219.054264
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
│       │   ├── last_modified_utc: 1696351005.0
│       │   ├── last_accessed_utc: 1698281240.6577516
│       │   └── created_utc: 1698281219.0542934
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
│       │   ├── last_modified_utc: 1696351005.0
│       │   ├── last_accessed_utc: 1698281241.3636642
│       │   └── created_utc: 1698281219.0543172
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
│       │   ├── last_modified_utc: 1696351005.0
│       │   ├── last_accessed_utc: 1698281240.671807
│       │   └── created_utc: 1698281219.0543463
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
│       │   ├── last_modified_utc: 1696351005.0
│       │   ├── last_accessed_utc: 1698281240.651523
│       │   └── created_utc: 1698281219.0544872
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
│       │   ├── last_modified_utc: 1696351005.0
│       │   ├── last_accessed_utc: 1698287091.621903
│       │   └── created_utc: 1698281219.0545151
│       └── content: <content could not be loaded>
├── quality.rst
│   ├── type: file
│   └── content
│       ├── file_name: quality.rst
│       ├── file_type: .rst
│       ├── file_stats
│       │   ├── bytes: 11330
│       │   ├── last_modified_utc: 1696351005.0
│       │   ├── last_accessed_utc: 1698281240.6689107
│       │   └── created_utc: 1698281219.0545485
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
│       │   ├── last_modified_utc: 1696351005.0
│       │   ├── last_accessed_utc: 1698281240.6714048
│       │   └── created_utc: 1698281219.0545783
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
│       │   ├── bytes: 795
│       │   ├── last_modified_utc: 1696351005.0
│       │   ├── last_accessed_utc: 1698281240.645629
│       │   └── created_utc: 1698281219.0546024
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
│       │   ├── last_modified_utc: 1696351005.0
│       │   ├── last_accessed_utc: 1698281241.0057662
│       │   └── created_utc: 1698281219.0546327
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
│       │   ├── last_modified_utc: 1696351005.0
│       │   ├── last_accessed_utc: 1698281240.6680439
│       │   └── created_utc: 1698281219.0546665
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
│       │   ├── last_modified_utc: 1696351005.0
│       │   ├── last_accessed_utc: 1698287090.6109822
│       │   └── created_utc: 1698281219.054691
│       └── content: <content could not be loaded>
├── tutorials.rst
│   ├── type: file
│   └── content
│       ├── file_name: tutorials.rst
│       ├── file_type: .rst
│       ├── file_stats
│       │   ├── bytes: 13901
│       │   ├── last_modified_utc: 1696351005.0
│       │   ├── last_accessed_utc: 1698281241.373841
│       │   └── created_utc: 1698281219.0547223
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
│       │   ├── last_modified_utc: 1696351005.0
│       │   ├── last_accessed_utc: 1698281241.3585973
│       │   └── created_utc: 1698281219.0547478
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
│       │   ├── last_modified_utc: 1696351005.0
│       │   ├── last_accessed_utc: 1698281240.6698346
│       │   └── created_utc: 1698281219.054774
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
│       │   ├── last_modified_utc: 1696351005.0
│       │   ├── last_accessed_utc: 1698281240.6814237
│       │   └── created_utc: 1698281219.0548048
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
│       │   ├── last_modified_utc: 1696351005.0
│       │   ├── last_accessed_utc: 1698281240.6707754
│       │   └── created_utc: 1698281219.054829
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
│       │   ├── last_modified_utc: 1696351005.0
│       │   ├── last_accessed_utc: 1698281241.365643
│       │   └── created_utc: 1698281219.0548592
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
│       │   ├── last_modified_utc: 1696351005.0
│       │   ├── last_accessed_utc: 1698281240.6760252
│       │   └── created_utc: 1698281219.0548933
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
│       │   ├── last_modified_utc: 1696351005.0
│       │   ├── last_accessed_utc: 1698281241.0061889
│       │   └── created_utc: 1698281219.054922
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
│   │       │   ├── last_modified_utc: 1696351005.0
│   │       │   ├── last_accessed_utc: 1698287074.8340688
│   │       │   └── created_utc: 1698281219.053314
│   │       └── content: <content could not be loaded>
│   ├── always-complete.jpg
│   │   ├── type: file
│   │   └── content
│   │       ├── file_name: always-complete.jpg
│   │       ├── file_type: .jpg
│   │       ├── file_stats
│   │       │   ├── bytes: 1081847
│   │       │   ├── last_modified_utc: 1696351005.0
│   │       │   ├── last_accessed_utc: 1698287058.4505665
│   │       │   └── created_utc: 1698281219.053346
│   │       └── content: <content could not be loaded>
│   ├── collapse.png
│   │   ├── type: file
│   │   └── content
│   │       ├── file_name: collapse.png
│   │       ├── file_type: .png
│   │       ├── file_stats
│   │       │   ├── bytes: 224248
│   │       │   ├── last_modified_utc: 1696351005.0
│   │       │   ├── last_accessed_utc: 1698287062.1483612
│   │       │   └── created_utc: 1698281219.0533714
│   │       └── content: <content could not be loaded>
│   ├── django-tutorial-example.png
│   │   ├── type: file
│   │   └── content
│   │       ├── file_name: django-tutorial-example.png
│   │       ├── file_type: .png
│   │       ├── file_stats
│   │       │   ├── bytes: 102306
│   │       │   ├── last_modified_utc: 1696351005.0
│   │       │   ├── last_accessed_utc: 1698287066.7762365
│   │       │   └── created_utc: 1698281219.0534122
│   │       └── content: <content could not be loaded>
│   ├── old-recipe.jpg
│   │   ├── type: file
│   │   └── content
│   │       ├── file_name: old-recipe.jpg
│   │       ├── file_type: .jpg
│   │       ├── file_stats
│   │       │   ├── bytes: 316167
│   │       │   ├── last_modified_utc: 1696351005.0
│   │       │   ├── last_accessed_utc: 1698287070.0839431
│   │       │   └── created_utc: 1698281219.0534418
│   │       └── content: <content could not be loaded>
│   ├── diataxis-white-416.png
│   │   ├── type: file
│   │   └── content
│   │       ├── file_name: diataxis-white-416.png
│   │       ├── file_type: .png
│   │       ├── file_stats
│   │       │   ├── bytes: 14872
│   │       │   ├── last_modified_utc: 1696351005.0
│   │       │   ├── last_accessed_utc: 1698287063.3084445
│   │       │   └── created_utc: 1698281219.0534687
│   │       └── content: <content could not be loaded>
│   ├── django-how-to-example.png
│   │   ├── type: file
│   │   └── content
│   │       ├── file_name: django-how-to-example.png
│   │       ├── file_type: .png
│   │       ├── file_stats
│   │       │   ├── bytes: 178399
│   │       │   ├── last_modified_utc: 1696351005.0
│   │       │   ├── last_accessed_utc: 1698287065.455899
│   │       │   └── created_utc: 1698281219.0534947
│   │       └── content: <content could not be loaded>
│   ├── overview-reference.png
│   │   ├── type: file
│   │   └── content
│   │       ├── file_name: overview-reference.png
│   │       ├── file_type: .png
│   │       ├── file_stats
│   │       │   ├── bytes: 48636
│   │       │   ├── last_modified_utc: 1696351005.0
│   │       │   ├── last_accessed_utc: 1698287072.4852784
│   │       │   └── created_utc: 1698281219.053519
│   │       └── content: <content could not be loaded>
│   ├── total-collapse.png
│   │   ├── type: file
│   │   └── content
│   │       ├── file_name: total-collapse.png
│   │       ├── file_type: .png
│   │       ├── file_stats
│   │       │   ├── bytes: 139903
│   │       │   ├── last_modified_utc: 1696351005.0
│   │       │   ├── last_accessed_utc: 1698287075.1163647
│   │       │   └── created_utc: 1698281219.05355
│   │       └── content: <content could not be loaded>
│   ├── overview.png
│   │   ├── type: file
│   │   └── content
│   │       ├── file_name: overview.png
│   │       ├── file_type: .png
│   │       ├── file_stats
│   │       │   ├── bytes: 209013
│   │       │   ├── last_modified_utc: 1696351005.0
│   │       │   ├── last_accessed_utc: 1698287073.3668716
│   │       │   └── created_utc: 1698281219.0535781
│   │       └── content: <content could not be loaded>
│   ├── ginger.jpg
│   │   ├── type: file
│   │   └── content
│   │       ├── file_name: ginger.jpg
│   │       ├── file_type: .jpg
│   │       ├── file_stats
│   │       │   ├── bytes: 235835
│   │       │   ├── last_modified_utc: 1696351005.0
│   │       │   ├── last_accessed_utc: 1698287067.3760278
│   │       │   └── created_utc: 1698281219.0536098
│   │       └── content: <content could not be loaded>
│   ├── overview-how-to.png
│   │   ├── type: file
│   │   └── content
│   │       ├── file_name: overview-how-to.png
│   │       ├── file_type: .png
│   │       ├── file_stats
│   │       │   ├── bytes: 44451
│   │       │   ├── last_modified_utc: 1696351005.0
│   │       │   ├── last_accessed_utc: 1698287072.0706952
│   │       │   └── created_utc: 1698281219.0536344
│   │       └── content: <content could not be loaded>
│   ├── diataxis-white-original.png
│   │   ├── type: file
│   │   └── content
│   │       ├── file_name: diataxis-white-original.png
│   │       ├── file_type: .png
│   │       ├── file_stats
│   │       │   ├── bytes: 63583
│   │       │   ├── last_modified_utc: 1696351005.0
│   │       │   ├── last_accessed_utc: 1698287063.555322
│   │       │   └── created_utc: 1698281219.0536644
│   │       └── content: <content could not be loaded>
│   ├── divio-explanation-example.png
│   │   ├── type: file
│   │   └── content
│   │       ├── file_name: divio-explanation-example.png
│   │       ├── file_type: .png
│   │       ├── file_stats
│   │       │   ├── bytes: 142553
│   │       │   ├── last_modified_utc: 1696351005.0
│   │       │   ├── last_accessed_utc: 1698287064.805648
│   │       │   └── created_utc: 1698281219.0536933
│   │       └── content: <content could not be loaded>
│   ├── anselmo.jpg
│   │   ├── type: file
│   │   └── content
│   │       ├── file_name: anselmo.jpg
│   │       ├── file_type: .jpg
│   │       ├── file_stats
│   │       │   ├── bytes: 428662
│   │       │   ├── last_modified_utc: 1696351005.0
│   │       │   ├── last_accessed_utc: 1698287061.7621872
│   │       │   └── created_utc: 1698281219.0537176
│   │       └── content: <content could not be loaded>
│   ├── overview-explanation.png
│   │   ├── type: file
│   │   └── content
│   │       ├── file_name: overview-explanation.png
│   │       ├── file_type: .png
│   │       ├── file_stats
│   │       │   ├── bytes: 55466
│   │       │   ├── last_modified_utc: 1696351005.0
│   │       │   ├── last_accessed_utc: 1698287071.5830383
│   │       │   └── created_utc: 1698281219.053749
│   │       └── content: <content could not be loaded>
│   ├── partial-collapse.png
│   │   ├── type: file
│   │   └── content
│   │       ├── file_name: partial-collapse.png
│   │       ├── file_type: .png
│   │       ├── file_stats
│   │       │   ├── bytes: 129799
│   │       │   ├── last_modified_utc: 1696351005.0
│   │       │   ├── last_accessed_utc: 1698287073.8602042
│   │       │   └── created_utc: 1698281219.053779
│   │       └── content: <content could not be loaded>
│   ├── diataxis.png
│   │   ├── type: file
│   │   └── content
│   │       ├── file_name: diataxis.png
│   │       ├── file_type: .png
│   │       ├── file_stats
│   │       │   ├── bytes: 156896
│   │       │   ├── last_modified_utc: 1696351005.0
│   │       │   ├── last_accessed_utc: 1698287064.2615159
│   │       │   └── created_utc: 1698281219.053807
│   │       └── content: <content could not be loaded>
│   ├── operation.jpg
│   │   ├── type: file
│   │   └── content
│   │       ├── file_name: operation.jpg
│   │       ├── file_type: .jpg
│   │       ├── file_stats
│   │       │   ├── bytes: 264617
│   │       │   ├── last_modified_utc: 1696351005.0
│   │       │   ├── last_accessed_utc: 1698287071.172176
│   │       │   └── created_utc: 1698281219.053836
│   │       └── content: <content could not be loaded>
│   ├── overview-tutorials.png
│   │   ├── type: file
│   │   └── content
│   │       ├── file_name: overview-tutorials.png
│   │       ├── file_type: .png
│   │       ├── file_stats
│   │       │   ├── bytes: 42443
│   │       │   ├── last_modified_utc: 1696351005.0
│   │       │   ├── last_accessed_utc: 1698287072.933839
│   │       │   └── created_utc: 1698281219.0538657
│   │       └── content: <content could not be loaded>
│   ├── mcgee.jpg
│   │   ├── type: file
│   │   └── content
│   │       ├── file_name: mcgee.jpg
│   │       ├── file_type: .jpg
│   │       ├── file_stats
│   │       │   ├── bytes: 152303
│   │       │   ├── last_modified_utc: 1696351005.0
│   │       │   ├── last_accessed_utc: 1698287069.4560788
│   │       │   └── created_utc: 1698281219.0538893
│   │       └── content: <content could not be loaded>
│   ├── recipe.jpg
│   │   ├── type: file
│   │   └── content
│   │       ├── file_name: recipe.jpg
│   │       ├── file_type: .jpg
│   │       ├── file_stats
│   │       │   ├── bytes: 208426
│   │       │   ├── last_modified_utc: 1696351005.0
│   │       │   ├── last_accessed_utc: 1698287074.3088856
│   │       │   └── created_utc: 1698281219.053914
│   │       └── content: <content could not be loaded>
│   ├── liquorice.png
│   │   ├── type: file
│   │   └── content
│   │       ├── file_name: liquorice.png
│   │       ├── file_type: .png
│   │       ├── file_stats
│   │       │   ├── bytes: 1189299
│   │       │   ├── last_modified_utc: 1696351005.0
│   │       │   ├── last_accessed_utc: 1698287068.5048187
│   │       │   └── created_utc: 1698281219.0539384
│   │       └── content: <content could not be loaded>
│   ├── diataxis-white.png
│   │   ├── type: file
│   │   └── content
│   │       ├── file_name: diataxis-white.png
│   │       ├── file_type: .png
│   │       ├── file_stats
│   │       │   ├── bytes: 47911
│   │       │   ├── last_modified_utc: 1696351005.0
│   │       │   ├── last_accessed_utc: 1698287063.8879755
│   │       │   └── created_utc: 1698281219.053969
│   │       └── content: <content could not be loaded>
│   └── django-reference-example.png
│       ├── type: file
│       └── content
│           ├── file_name: django-reference-example.png
│           ├── file_type: .png
│           ├── file_stats
│           │   ├── bytes: 146194
│           │   ├── last_modified_utc: 1696351005.0
│           │   ├── last_accessed_utc: 1698287066.1541855
│           │   └── created_utc: 1698281219.053997
│           └── content: <content could not be loaded>
├── _templates/
│   ├── page.html
│   │   ├── type: file
│   │   └── content
│   │       ├── file_name: page.html
│   │       ├── file_type: .html
│   │       ├── file_stats
│   │       │   ├── bytes: 1624
│   │       │   ├── last_modified_utc: 1696351005.0
│   │       │   ├── last_accessed_utc: 1698281240.6705015
│   │       │   └── created_utc: 1698281219.0542238
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
│               │   ├── last_modified_utc: 1696351005.0
│               │   ├── last_accessed_utc: 1698281240.6704924
│               │   └── created_utc: 1698281219.0541909
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
            │   ├── last_modified_utc: 1696351005.0
            │   ├── last_accessed_utc: 1698281240.689363
            │   └── created_utc: 1698281219.054433
            └── content: @import 
                url('https://fonts.googleapis.com/css2?family=Source+Sans+Pro:it
                al@0;1&family=Source+Serif+P
                ...
                :last-child th {border-bottom: none;}
                table.docutils thead {border-bottom: 1px solid var(--orange);}


```

