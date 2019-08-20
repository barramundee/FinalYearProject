
# 6COSC006W – Final Year Project Report

# Developing a Web-Based Planning Tool to aid the Implementation of Agile Working in a Corporate Environment

### Pedro Fernandes (w1577152)
### Supervisor: Alexander Bolotov
<br>
This report is submitted in partial fulfillment of the requirements for the BSc (Hons) Software Engineering degree at the University of Westminster.
<br>
School of Computing & Engineering
University of Westminster
02/05/2019 

# Declaration
<br>
  This report has been prepared based on my own work. Where other published and unpublished source materials have been used, these have been acknowledged in references.

<br>

* Word Count: 14,696
* Student Name: Pedro Fernandes
* Date of Submission: 02/05/2019

# Abstract
<br>
  The sequential “waterfall method” of software development has been waning in popularity in recent years and “Agile Working” has emerged as a leading methodology in organisations involved in development projects. However, despite the increased focus, there are a surprising number of individuals that are unfamiliar with Agile as a whole, as well as the various subsets of it that are also used. In addition, even without lack of relevant knowledge, there can be issues successfully joining a team that is using Agile development, from a lack of defined roles to a general misinformation and disinterest in changing their way of working. Many of these issues arise however, from the misuse of an Agile Methodology or the bad implementation of one.

  In order to facilitate the implementation of Agile working, some games and planning applications have been developed to help teams learn the processes involved. However, they can be quite general and over simplified. Furthermore, most of those games are targeted to those Teams who already have decided on what methodology they ought to use in an upcoming project or have already implemented its framework – this leaves a wide section of users that are not sure what methodology to use or how to implement it as a whole. Therefore, an application has been developed to provide guidance on which subset of Agile is the most appropriate to use, helping the user to learn more about the process as well as making the implementation more successful by being more relevant to the individual project. Such an application will then be used to track the progress of each project, as well as allowing the user to view the achievements of other team members, allowing projects to be worked on remotely, and for product owners to keep track of the overall progress and make suggestions throughout development. This will ensure that a User or Team that is unsure about what methodology they should use in an upcoming development project is/are guided properly with enough information to implement an Agile framework correctly. Its design and implementation will be discussed and, additionally, the general issues that arise when attempting to develop an application that makes a decision for the User, briefly touching on types of AI that are usually used for these projects and their advantages / disadvantages.
  
  Furthermore, this project will also document some findings from research regarding the effectiveness of an Agile methodology, its implementation as well as its overall success when implemented properly in a professional organisation, contrasting some additional research that was performed on both software development professionals and professional workers from non-technical backgrounds in a company that has just began implementing an Agile Way of Working. It was found that although the engineers that had a properly implemented methodology were completely fluent and versed in the ways of working in an Agile company, the majority of people that had the Agile way of working forced onto their departments had badly interpreted Agile as a whole, resulting in a negative experience and in most of the cases, had given up on Agile.

# Acknowledgements
<br>
First and foremost, I have to thank my dad, mum and sister, who always supported and helped me pursue my dream of graduating as a Software Engineer in the UK. Without their trust, I fully believe I would never have become someone they’re proud to look up to.

Secondly, I would like to thank everyone at ELBA, and in particular Sally Roberts, for believing in me and giving me to opportunity to partake in a year-long internship at ING London. I would also like to thank everyone I have met there, in particular Wouter Wezelman, for giving me an opportunity to complete my studies while getting valuable experience as a Development Engineer and working in an environment that allowed me to meet some of the most honest, kind and genuine people I would never otherwise have had the opportunity to meet.

I would also like to thank Dr. Alexander Bolotov, for allowing me to develop a project that both of us were passionate about, as well as providing guidance that this report much needed.

Last but not least, to Kellie, for constant support throughout my final year of University and pushing me to do my best work possible.

# 1. Introduction

## 1.	Problem Statement 
<br>
  For many years, software development in corporations has relied on a sequential approach to its product creation, called the “Waterfall Model”: the central idea of this approach is to spend the majority of resources (time, money and effort) up-front. There are advantages to this methodology, such as being well-suited for projects where the quality of the final product is emphasised over costs and time, being relatively simple to implement and the inflexibility of the model simplifying project management. It is when we start looking at the disadvantages of this methodology, that we begin to see how the Waterfall Model might not be appropriate for use in today’s business world. Having been developed in the 1970’s to prevent costly revisions late in a development of a product, it is not well-suited for lengthy or large-scale projects. Additionally, the lack of flexibility in this model means that the final outcome of the project is based on its initial requirements (which, as one might expect, are bound to change during the project’s development). However, the main disadvantage of this methodology is since the model puts most of the work up-front, the final product is not produced until very late in the project.

  Recently, there has been a call for more efficient ways of working and the Agile methodology has become rapidly popular in many companies, with its implementation being rolled out across Europe. Agile, as stated by its manifesto, is “the ability to create and respond to change. It is a way of dealing with and succeeding in an uncertain environment”. Agile, however, is an umbrella term for many different frameworks and practices, allowing the creation of new ways of working on the go. Thus, many companies might adapt one version of Agile completely different and unique to what other companies might be using. One crucial aspect that separates Agile from the waterfall method is the focus is on the people doing the work and how to co-operate with each other. Collaboration is a big ideology in this model, encouraging users to cross-work between teams. As there are no typical roles in the Agile model, such as a manager, teams are instead built based on the user’s skill set, and the manager equivalent role will instead step-back and let their team explore and decide how they are going to deliver products and organise themselves, and only step in when the team are unable to resolve issues.

  However, with such a new method, a key problem has been highlighted- a high percentage of young graduates and business professionals have either no knowledge of this methodology, never used it in action or are simply disinterested. This could be down to a lack of education on the Agile way of working, both in theory or in practice, or because it is poorly implemented in many companies. Furthermore, now more than ever, more software development companies require employers to have some, if not a lot of experience dealing with the Agile way of working.  
	Therefore, to help implement the Agile way of working in corporations, I plan to build a web application to that will serve as a platform to facilitate Agile projects, act as a bridge between employees or students using the methodology and can be used to educate those unfamiliar with the practice.

## 2.	Aim and Objectives
<br>
  My aim, once I have finished developing the web app, is to have produced a fully functional, ready to go, web-based application that will help the implementation of an Agile Methodology in both a business setting as well as for a simple project. By setting up their own profile and adding tasks to their profile, the user will be able to start their project quickly and efficiently using their desired methodology. The main feature of this project will be an Agile Picker using a self-made question tree that decides which the best Agile methodology is for any single project a user adds to the web app. This will be done through a series of queries that the user will answer regarding their project, from simple questions such as “how many team members?” and “deadline for this project”? to “what’s the estimate work distribution between team members?” and “how much work do you plan to do per week?”. Based on these questions, the app will then assign “points” to every methodology based on the answers the user gives, and at the end will display to the user what the methodology with the highest points, and thus most appropriate option, is.

  Once the questionnaire has been completed, the product owner (manager, external client, teacher, etc) will be able to create teams using the proposed methodology. Here, the team members, or players, can also register and join the appropriate team, creating a virtual meeting and planning space for the project. The product owner will then be able to assign tasks to each player, through the various planning apps which will be within my web app. The exact tasks available to allocate and the process will depend on the specific subset of Agile being used. Once the initial inputs are made, players will be able to create online sessions where they can discuss their assigned tasks, confirm the distribution of the activities and make any changes within the app for all to see. 
	
  Where the player is not familiar with the Agile way of working methodology or any of its subsets, there will be a “Learning” section, available at all times. Here players can access links, tutorials and other learning materials that are necessary for a user to become fluent in this new “language”. It is also planned for there to be a section where users can ask each other questions on the Agile process, outside of their individual teams, to further facilitate the learning process. Should the application be developed further outside of the Final Year Project requirements, the product owner would be able to view the progress of everyone from within the task. This would be in the form of an easy-to-read graph in order to facilitate the communication between the product owner and players, as all will easily be able to see the project’s progress and the overall time-scale, and make any necessary suggestions for improvement as the tasks go on.

 
# 2. Background

## 2.1 Literature survey	
<br>
  The increase in Agile’s popularity has also lead to many studies to be conducted into its effectiveness. Cooke (2012), stated that Agile can increase the quality and value of software development, as well as overcoming the traditional issues in the development process such as exceeding budgets, missing deadlines, poor-quality work and unhappy final users. Cooke further states that Agile, regardless of its subset, is intended to adapt to changing requirements throughout the project, deliver continuous value to the organisation, place trust and control in team members, and encourage feedback between the team themselves, the wider organisation and the client.  

  While in theory, Agile can improve efficiency and lead to rapider software development, many studies have been conducted into Agile’s applicability in real-life development projects. The most frequent issue with Agile highlighted in the existing literature, appears to be changing IT staff’s mindsets to adapt to the new way of working. As stated by Patanakul and Rufo-McCarron (2018), the Agile methodology needs to be integrated with existing processes, tools and customer requirements to be effective. Younes et al (2018) highlighted the need for a system which can detect lack of communication and other weaknesses in team members. Although my app will not do this on an automated level, it will be able to help identify such issues. There are also possible risks of managers fearing they may lose control of the team or project, again, such an application will enable them to get a detailed overview of the process and make suggestions.
  
  According to Paptheocharous and Andrea (2014), Agile needs to focus more on the individual team members, rather than the exact processes. They emphasised that a successful Agile project should adapt to the strengths of the team. The app I propose to develop should correspond with this, by giving each team member a platform to highlight their strengths and weaknesses. Furthermore, Conboy, Coyle, Wang & Pikkarainen (2011) stated that in Agile working, tools and processes should be less of a focus than the individuals in the team, the roles which have been assigned to them, and how they interact together.
  
  A literature review conducted by Dikert et al (2016) found that Scrum was the most common Agile method used in transformation projects. As I will also be using my knowledge of Scrum to build the website, it is affirming to know it has popularity elsewhere, although other Agile subsets will be available to use on my application. 
  
  Rola et al (2016) listed some key requirements for an Agile (Scrum) team, which I will aim to integrate into my web app; the need to facilitate verbal communication, the ability to continuously show information indirectly, a co-operative team environment and to support an information exchange. Ben-David et al (2012), however, raised concerns that the Agile method may be difficult to implement because its cycle it different to other business processes, especially in cases when payments are made at specific points in the project. They suggested tailoring Agile to accommodate this and vice-versa. As my application could be opened up to the customers and other stakeholders so they are able to have a better view of the progress being made.
  
  An article by Papadopoulous (2015) focused on the organisation of the team to ensure maximum efficiency and success of the Agile process. He suggested that having connected, self organising teams in an organisation with less of a hierarchal structure can allow closer collaboration and reduce complications. This is where Agile differs from more traditional methodologies, which often reply on heavy documentation and reporting to successively more senior staff. Papadopolous’s research also highlighted the effect of development methodologies when teams are dispersed. He suggested that the Waterfall approach may be superior in circumstances where team members are in a different location due its reliance on heavy documentation, which means information can be passed clearly and in detail. Agile methodologies however are more focused on an informal feedback method and require more face to face communication between the participants because of its nature. However, as more corporations are becoming more open to flexible working, such as working from home or collaborating with teams in other countries, it presents an opportunity for my app to provide the documentation of the development process in an easily accessible place.
  
  The existing literature has often focused on the successful implementation of Agile working, however, less has focused on the sustained usage of the methodology. Hsieh and Zmud (2006) and Saga and Zmud (1994) detailed three phases for sustained usage of a new process: acceptance, routinisation, and infusion. The last of these also encompasses extensive use, integrated use to enhance work, and emergent use to go beyond the original scope of the process. I aim for my application to be key to sustained usage of Agile in organisations due to its support of different subsets, offering flexibility, and allowing the stakeholders control over the project and giving them the option to customise and use the application in the way which suits themselves and their teams best. 



## 2.2 Review of projects / applications
<br>
  Although there are many applications in the market already that are quite similar to what I aim to build, they all lack the important aspect in which they don’t let the user actually decide for themselves what Agile methodology they want to use. Instead, my app aims to help the user decide, by having a series of questions determined to pick the most appropriate Agile methodology.  Furthermore, most apps currently on offer are only meant for the user to use once or twice during their sprint, whereas my web application incentivizes both an initial use at the beginning of a project’s implementation, as well as constant use and monitoring during the project’s lifecycle.

PLANITPOKER	Allows users using the Scrum methodology to vote on how much their stories weigh.	Market leader as there’s not another stand-alone planning poker free-to-use application. Easy to set up a user session and to get multiple users connected.	No real use to users that don’t use SCRUM or want to use planning poker for stories.

JIRA	Dashboards, saved searches, workflow, issue navigator.	Customisation allows the user to adjust JIRA to any type of software.	High-learning curve, not viable for some development projects, clunky user interface.

TAIGA	Project management tool and cloud-based, with Slack and GitLab integrations.	Dedicated progress bar / indicator of what has been completed when informing clients of progresses.	Users have limited functionality in what they can do on the web app. Plus, it uses a pay scheme to add more projects to one account.

TASTYCUPCAKES	Provides multiple Agile planning games that may be used by any methodology.	Has both training apps, as well as planning ones that help users plan their stories during a project’s lifecycle.	The web app assumes that an user already know whats methodology they will be using in their project’s development, meaning that a User that does not know what Agile is will be left at a disadvantage when using this app.

SERVICENOW	Similar to JIRA, it helps management of product and software development lifecycles.	Accurately shows planning to Users and allows easy access to Story management across sprints, backlogs and epics.	Is restricted to only Scrum or Waterfall methodologies.

  The above mentioned Agile applications were the ones where research was focused upon. From an initial search, it was found that most applications were behind a pay-wall that required the user to pay up-front to use most of the tools the website provided. Additionally, in some ways, some applications looked to be exactly the same as their counterparts – it was almost like they were all developed by a single person and then branched out, emphasizing a lack of originality and design. One interesting aspect however, was that out of all these applications, none of them offered my app’s unique selling point – the ability to decide for the user based on a series of queries what the most appropriate Agile methodology should be used for the project. Further research was attempted at trying to find an application that was only focused on the training / assistance to pick an Agile methodology, but no similar projects were found – which incentivizes the need for my Project’s success and implementation.
	PlanitPoker is on its own, like many of the above-mentioned applications, is just a planning Agile tool for a specific methodology. It’s not a dashboard or a platform where users can save theirs tasks, but merely evaluate the weight of these tasks. That said – if a similar version would be implemented in my app, it would make more sense to keep everything under a single “umbrella” – furthermore, like above mentioned, a key difference that makes my project stand out is an Agile Picker which I have not been able to find similar projects to. Furthermore, it seems like most Agile applications out there in the market are strictly for business use – meaning they’re behind a “pay wall” if you want to benefit from the applications full benefits. Although this may work in the favour of those who created said app, it also assumes that a User is already ready to start their project and are 100% confident in what methodology they want to use.  Another interesting aspect would be that should I, the developer of this app, be put into a position where I would have to manage a newly formed Agile team and would have to decide for myself what the best Agile methodology to use would be, the only course of action would be to research into each methodology individually or try to find journals documenting the differences between each other. Here’s where the real need for my application comes in – by tailoring the questions for the User depending on his/her needs, the application suggests the best methodology based on the User’s answers, making it almost like a personal assistant when deciding a project’s methodology.

## 2.3 Review of tools and techniques
### 2.3.1 Django

  One of the goals for the development of my final year project was to push myself to learn and use something I wasn’t quite familiar with. Since I decided to develop a web application, it would only make sense for me to use a language / application I had never used before. In university lectures, we were taught how to use Netbeans and Java, with a brief introduction to HTML and JavaScript in year one. Although I was keen on using the latter, I understood the boundaries of just using HTML and JavaScript as my main languages. That was when I came across Django: a “high-level Python Web framework that encourages rapid development and clean, pragmatic design”. I found this to be perfect, as Python is a language that is becoming quite popular in many work environments as of 2019, with the ability to automate a wide variety of tasks, as well as me not being very familiar with the language. Furthermore, I was very surprised at the amount of documentation that the Django website provided (https://docs.djangoproject.com/en/2.1/). Another feature Django has that made web application developing easy, was how easy it was to understand why something worked or sometimes, why it didn’t work. One issue that many programmers have with their code is that sometimes, when an error shows up, most times they are clueless as to why the code isn’t working. Django fixes this by giving dedicated error messages, allowing a quick fix without requiring an extensive search on websites for a solution.  
  This allowed for time saving as well as understanding the code clearly – in a way, this helped me learn HTML and Python better. The tutorial for new users was also very easy to read and follow. Even though if you don’t have any programming language whatsoever, it has a dedicated section for that. It also provides an “all-inclusive” experience, meaning it sets up automatically an admin panel, ORM, database interfaces and a directory structure for all the apps you choose to code within it. Although Django proved to become one of my favourite languages that I choose to use now on a day to day basis, I found the initial leap from typical HTML programming to using a fully-fledged web framework quite massive. One problem I had with Django initially was that there were too many “.py” files that seemed like they were just there for no reason. For example, the “views.py” file was particularly confusing, as my initial understanding was that all the data that were to be parsed onto the database would be written in the actual “.html”. However, much of the code as you can see below had to be written on the “views.py” in order for it make a connection to the .html file in question.
  
    class ProfileView(TemplateView):
    template_name = 'home/profile.html'
    model = Profile

    def profile(self, request):
        args = {'user': request.user}
        return render(request, 'home/profile.html', args)

    def post(self, request):
        p = request.POST
        action = request.POST.get('action', '')

        if action == 'create':
            Tasks.objects.create(profile=p['profile'], username=p['user'], task=p['task'], type="todo", points=p['points'])
            return render(request, 'home/profile.html')

        if action == 'thumbsup':
            r = request.POST
            vote = Tasks.objects.get(task=r['comment'])
            vote.votes += 1
            vote.save()
            return render(request, 'home/profile.html')

        if action == 'thumbsdown':
            r = request.POST
            vote = Tasks.objects.get(task=r['comment'])
            vote.votes -= 1
            vote.save()
            return render(request, 'home/profile.html')

Although this didn’t apply to me, the installation can be quite daunting to unexperienced programmers, as there were a lot of packages and dependencies one had to install to get the best experience possible. Furthermore, if you don’t have Python installed on your machine, that’s another thing you need to install to get Django fully working.

### 2.3.2 PyCharm

As I was keen on expanding my knowledge in Python, instead of Netbeans I settled with using PyCharm – a Python IDE that provides a lot of assistance with Python code. One of its most impressive aspects is its intelligent code completion. Though it doesn’t write code for you, I found myself using it more often than I would Google pieces of code. It also boasts an incredible package management option, allowing me to access Django documentation on the go. On the back-end side of things, PyCharm’s database integration (specifically sqlite3 with Django) made it really easy to manage my objects while I was programming the web app initially. It’s not all about Django though – Python does support a wide variety of languages and I still haven’t used it to its full potential. I am aware it has an option to create Jupyter notebooks which I believe is very useful for data science projects. One negative aspect about it is that it uses 8 GB of ram and for most people that’s quite a lot. Also, if you’re not a student then you would have to pay for the professional edition, and that can be quite off putting to some.

 
# 3. Requirements

## 3.1 Stakeholders
<br>
 In the initial stages of the project’s development, I as the designer, builder and maintainer will be the only user of the app and the only one affected by its development. However, after the extensive testing phase, a demo version will be produced and uploaded to a dedicated server and put online. At this stage a small group of users will be able to use the application’s features, allowing them to highlight both the positives and negatives of the project.
	Once the product has reached a more advanced developmental stage, the number of stakeholders will increase greatly.  These will be the users of the app, in different positions such as the players, product owners and clients, as well as wider employees of the corporation who are exposed to projects in less direct capacities.

## 3.2 Gathering requirements 

  Having worked in a software development team that only recently started to adapt the Agile way of working, I saw first-hand how a company implements Agile (specifically Scrum). During my placement, I was tasked to create a planning poker tool to help my team stay organised and to gamify their activities: it was a consensus-based planning tool that allowed the user to estimate effort or relative size for the stories (tasks) each team tackles every two weeks (a sprint). The app was then dispersed amongst the rest of the organisation and is now being used by all teams to implement the Agile method of working in all teams in ING Bank in London. Through this, I managed to understand what the requirements were to build an Agile app, which directly influenced my decision on what the theme of my Final Year Project was.
	In order to verify the usefulness of the project, a small-scale study was conducted amongst 20 software development professionals working for a large corporate organisation which had recently introduced an Agile working policy to understand what the most important aspect of an Agile web application would be.
	The study found that these software engineers were more focused on having a web app that was easy to use rather than having a lot of tools. It’s interesting because it set me on a direction of trying to make sure the one app that was being developed (the algorithm picking Agile methodology) was at its cleanest state possible, rather than having an abundance of useless tools on its kit. However, following this small study, a broader study was performed on a larger group of 30 participants regarding an Agile Methodology’s usefulness. The questions were as follows:


    1.	What is your current knowledge of Agile working?

    a)	I am familiar with Agile working and I have used in in a project
    b)	I know about Agile working, but I have not used it in a project
    c)	I have heard of Agile working, but I don't know what it is
    d)	I have never heard of Agile. 


  This question was asked to ascertain user’s familiarity with Agile working. Most of the respondents stated they were familiar with Agile working, and most said they had an understanding of what it entails. However, this is not surprising, as the sample of individuals questioned were mostly IT professionals in an organization that has just recently. Therefore, most of the participants have been exposed to Agile in some capacity, with some already using it to develop projects. Consequently, this result should be treated with caution, as it is likely not a representative sample of workers and their experiences. 

    2. Which Agile subsets are you familiar with? 
    a)	Scrum 
    b)	Kanban
    c)	Lean
    d)	Extreme Programming (XP)
    e)	Crystal 
    f)	None of these


  This question was to identify the most popular/commonly used subsets of Agile. The results show that Scrum is by far the most popular methodology. While this result is to be expected, as the organisation is question predominantly uses Scrum, it is also supported as the most common method by the existing literature as well. Crystal was one of the least well-known subsets, potentially because of the limited amount of information publicly available for it. XP, alongside Lean, was also one of the more unpopular methodologies, this could be due to it being difficult to implement in practice as it offers little flexibility for users. The application will be beneficial to those who like to use the established methodologies, and those who could benefit from discovering the more obscure ones.


    3.  Would you say your view of Agile working is:
    a)	Positive
    b)	Negative
    c)	Neither positive or Negative
    d)	No opinion/prefer not to say


  Overall, most of those asked had a positive perception of Agile working, which suggests there would be good support for my application. However, it also presents an opportunity to make Agile more appealing to those who currently don’t have a favourable opinion of the approach, by making it easy to learn the different methodologies and simplifying the product development process via the planning tools. 



    4. Would you find an application to assist selection of an Agile methodology useful?
    a)	Yes
    b)	No
    c)	Don’t know 



  Most of the participants asked said they would find the Agile planning application beneficial. This is of course highly encouraging and suggests the product has the potential to add value to the individuals and the organisation as a whole. Those that said Don’t know might be those that have answered they hadn’t heard about those Agile Methodologies


    5. What features of an Agile application would be most useful to you?
    a)	Easy to use
    b)	Tool abundance
    c)	Squad integration
    d)	Task management 
    e)	Team visibility
    f)	Project management 
    g)	Planning board 


  Of the options for features for the application, ease of use was the most popular. This is of course essential as it will need to appeal to individuals of all different backgrounds and experience levels. There is also an expectation of most software these days to be intuitive to use and not require extensive training or guidance, this will be important to keep in mind when developing the application. However, personally I believe all the elements listed in the questionnaire are highly relevant and important in making the application a high quality and useful product, therefore I intend to integrate all of the features into the final product. 



## 3.3 Modelling requirements and relevant diagrams

  When development of this project started, it was important to outline what the main requirements were in order to have a working prototype. Thus, when modelling the requirements needed, these were split into two distinct groups – the first one would be the front-end, meaning how the code looked (HTML, CSS), and the other one would be the back-end, meaning how the code behaved in the background (database, functions). 

  For the use case diagram, I tried to keep it as simple as possible to showcase the difference between a Team Manager and a Team Member in my project. Although they will be able to access the same features, only a Team Manager will be able to create a Team and add Members to it. Once in it, I plan to add a hierarchy to decide who can add stories to the team’s backlog. Although this is a small part of the overall code and project, it was important to include this difference to keep in mind when developing extra features for the code.

  Above you can look at the overall hierarchy of the Project’s code. Most of the code is generated around a “User”, which is created every time someone registers. For each user, there will be a profile to exist multiple teams, and any one team can have multiple users. Another section associated with it (a one to one relationship). Around those, there are other models that use both of those models’ information, such as Teams. This will be a one to many relationships as it will be expected that one Team will have a lot of Users, and any single User might have a different number of teams. As of this project’s requirements, very basic models are being implemented into the code, like the Tasks, that just takes a String and stores it, alongside whose Task it belongs to and how many story points it has been assigned. 

  For the main application, the Agile Picker, research was conducted into each methodology in order to create a list of questions to make sure the correct methodology was picked. Furthermore, as SCRUM is the most well-known methodology, and since to other Users the other methodologies might not be known, it was important for this project’s aim that each methodology was well defined with its own principles and identity. To solve this issue, a lot of effort was put into creating a complex question tree that gave the user the feel that its answers were being taken into consideration when picking an Agile Methodology. As you can see above, from any given question, the User will always end up in one of the methodologies this project’s research was focused on – Scrum, Lean, Extreme Programming, Lean and Crystal. However, a problem arose from this method of deciding a methodology – a User that voted yes for five Scrum questions and yes for one XP question would get Scrum regardless, and my application would ignore the fact that the user responded positively to an XP query. This would create situations when perhaps a mix of methodology principles would be ideal for the User’s project. To solve this issue, a scoring system was created that would award points to each question based on the users answer, and at the end would display the score for each methodology. That way, even though a user might end up being suggested the Lean methodology, if there’s two points in the Scrum question line, the user might look up into what defines each of those methodologies, and apply a custom methodology into their own project development (for example, most software development teams that use Scrum end up, in some way, using XP’s principles or Kanban’s without realizing it).


## 3.4 List of project requirements 

ESSENTIAL	DESIRABLE	LUXURY
Registration
Login
Profile
Home Page
Personal Stories	Team Management
Social Element
Team Competition
Sprints
Team Stories
Squad Customization
Agile Planning Tools	AI Picking Agile Methodology
Research into every Agile Methodology proposed


Although the “AI Picking Agile Methodology” is categorized under “Luxury”, it will be the main aspect of the web app. Without it, it would simply be on the same baseline as the other apps that were reviewed on review of projects / applications section. The essential, are simply what a usual Agile web application would offer to its users – registration and login being the simpler ones. 
Another requirement that was essential for the success of this project was a thorough research into every methodology. Although the “main” project will be the code presented (something physical that can be tested), one of the main outcomes of this project is the research into every Agile Methodology that will be discussed further in this report, to make sure that an implementation of either of them is backed by a thorough knowledge.





## 3.5 Legal, social and ethical issues

  There will be a number of issues to consider when implementing this project into a large corporation or even if offering it to the wider public. Some of the projects that users may be utilising the app for could be of a highly sensitive nature, meaning a high level of privacy and security will be required to prevent other users, intentionally or not, from accessing projects from outside of their teams. Additionally, as use of the app requires users to create a profile, it will be necessary to comply with relevant laws regarding the gathering, use and storage of people’s personal data.
	Once more publicly available, the app will need to be located on a secure server, possibly utilising encryption for user information and passwords. Additionally, there may need to be terms and conditions for a user to agree to, to fulfil necessary legal requirements. If the app is used in a corporation, then it will also need to conform to that organisations rules and requirements. Furthermore, ahead of building the application, a small questionnaire was asked to participants to assess their understanding of the methodologies and their requirements for the product. In order to ensure the answers were recorded anonymously and the participants were aware of use of their answers and the right to withdraw, they were sent an ethical information and consent form prior to completing the survey. In addition, it was important to ensure the answers that were given were treated anonymously and securely stored, this was achieved by using a popular online surveying website which collected and processed the results.


# 4. Methodologies
<br>
  The key feature of the finished project will be the tool which helps the user select the most appropriate Agile methodology to use for their project. In order to do this accurately, it is necessary to improve knowledge and understanding of each method to incorporate it into the application. A good research topic that was crucial for this Project was what made each Agile Methodology special and different to each other – for the Agile Picker to work, the key differences between each other had to be clearly outlined, so it would be easier to create questions around them. The methodologies that were picked for this were Scrum, Kanban, XP, Lean and Crystal.
	Firstly, it’s important to stress what Agile is: it’s a set of principles that are based on an incremental approach to a project. This means that instead of having a big in-depth planning session at the start of a project, requirements may change over time. However, before talking about the differences between methodologies, it’s important to point out what similarities they all have. Under the Agile Manifesto, the 12 principles that an Agile Methodology must follow are:
1.	“Satisfy the customer through continuous delivery.”
2.	“Requirement changes are welcome even in late development.”
3.	“Deliver working software frequently.”
4.	“Business people and developers need to work together daily.”
5.	“Projects must be built around motivated individuals.”
6.	“Face-to-face conversation is the most efficient method to discuss information.”
7.	“Working software should be how you measure progress.”
8.	“Agile processes should promote sustainable development.”
9.	“Attention to technical excellence and good design enhances agility.”
10.	“Simplicity is essential.”
11.	“The best architectures and requirements emerge from teams that take it upon themselves to organise.”
12.	“Throughout a sprint, the team should gather and reflect how to become more effective.”
	As all of the above methodologies follow, in one way or another, the 12 principles mentioned above, it’s important to research in depth into each one to identify what are the “specific principles” of every one of those methodologies. 

## 4.1 Scrum

  Scrum might be the Agile Methodology people think of when Agile is mentioned. Indeed, from my research and multiple talks with both Software Engineers and Students who had no Agile knowledge, it was found that one might think that Scrum is synonymous with Agile.
To begin with, Scrum is a methodology mostly used for management. This means that is it only used to plan a sprint and to analyse how it went. Tasks are broken down so that they can be completed in a single sprint, and the team responds by committing a specific amount of work to it.  As far as roles go, there are three main concepts that are introduced when using the Scrum’s framework:
•	Development Team: this is where the developers, engineers and designers for example would be put into. These are usually small teams (between 6-10 people, from my experience) that will work in sprints to deliver working software.
•	Scrum Master: the person who hosts the Daily Scrum meetings, which generally follow the script of “What did you do yesterday?”, “What will you do today?” and “Any impediments?”.
•	Product Owner: this is the person who makes the connection between the development team and the stakeholders.

  Another aspect that distinguishes Scrum from the other frameworks is its workflow – sprint planning, sprint, and sprint review. Scrum, and the other frameworks that will be mentioned ahead, also uses an Agile element called artifacts (ways of sharing information / making information transparent). Scrum specifically though, has User Stories, Tasks, Backlogs, Sprint Backlogs and Extensions – for example, a planning poker game that lets users decide the weight / time required / effort required for a specific story.

## 4.2 Kanban

  One of the key aspects that defines Kanban is the mentality of avoiding production of extra resources. This is done by applying a cap to work that the team can have “in progress”. Furthermore, instead of being assigned tasks, one of the practises of Kanban is for team members to pick up work from a pool of available tasks, creating an atmosphere where one does what they’re capable of doing. Similar to Scrum, Kanban tracks the activities that are both “in-progress” and “done” – this number of activities cannot be exceeded by a number defined by the team’s manager (once again, limiting the amount of work that is being done at any single time). Its principles are as it follows:
•	Work visualization: by letting team members choose their tasks as they come, multitasking is reduced, and focus is increased.
•	Decrease waste: as work in progress is limited to avoid an endless income of tasks, waste should be almost non-existent if Kanban is applied properly.
•	Customer comes first: as work is picked up as it comes, this enforces a policy in which if a customer sends a request, it should be picked immediately by an available team member.

  A key difference however, between Scrum and Kanban, is that while Scrum works in 2 week sprints and the scrum board is reset between each sprint, Kanban is continuous and persistent – most of the work is unplanned, and because of this Kanban is mostly used in IT Support teams, for example. Hence, the team can re-prioritize tasks as they come. Many articles seem to want to have to user decide Scrum and Kanban and assume that they’re part of the same “philosophy”, whereas in fact Scrum falls under an Agile methodology, and Kanban fits better under a Lean methodology, as we’ll be looking into in the next few sections.
  
## 4.3 XP – Extreme Programming

  Extreme Programming (XP) is the third framework that could fit into the same category as Scrum. For a fact, most of the teams that use Scrum, or even Kanban, end up in some way using most of the practices of XP. 
At its core, XP is programming practices taken to the extreme. One of the most popular features includes pair programming (which is used instead of formal code reviews) – the purpose of this is to encourage communication and understanding of the problem. As most extreme cases, this methodology can be hit or miss. Since it requires every single one of its practices to applied correctly for it to work, it is not as flexible as the other frameworks that are covered in this report. Furthermore, little to no planning is usually made in XP, meaning that a project is many times designed on the go. The practices of XP are:
1.	“Test-Driven Development”: code is written quickly white maintaining the best quality possible through constant feedback – every line of code however, must be tested first in order to be released. 
2.	“Planning Games”: sharing a similarity with Scrum’s planning tools, the team meets with the customer at the beginning of a development cycle to discuss a possible project’s features.
3.	“Pair programming”: while one programmer focuses on writing the code, the second one must focus on code reviews, improvements and give suggestions, and in theory fixing mistakes along the way.
4.	“Customer is always on-site”: while this may be impossible in most projects, according to XP the customer must be ever-present in its constant development.
5.	“Code refactoring”: while this practice is already widely used by most programmers working in a business setting, XP uses this technique to double down on the code reviewing aspect, removing redundancy and unnecessary lines of code.
6.	“Continuous Integration”: as XP teams commit code multiple times a day, developers keep the system always fully integrated. This means that code can be re-used by the other team-members, effectively improving communication.
7.	“Small Releases”: an interesting aspect of XP’s methodology is releasing the product as fast as possible, even in its most basic state. This is works in XP’s context as developers can get constant feedback and slowly make small updated to it.
8.	“Coding Standards”: the programmers of a team under XP’s methodology must have a common set of coding practices for code writing – if code is written with the same rules it encourages the next practice, collective code ownership.
9.	“Collective Code Ownership”: as mentioned above, each team member can access and update code, encouraging cooperation.
10.	“Simple Design”: as mentioned in the XP’s manifesto, “the best design for software is the simplest one that works”. That means no duplicate code, contain the fewest possible lines of code, methods and classes, and it should be easy to read and to review.
11.	“System Metaphor”: the system must have a simple enough design that, should a developer that is not familiar with the project read or review the code, he will understand clearly what the intent of the programmer was.
12.	“No Overtime”: this is enforced through a strict 40-hour week – programmers should feel well and rested while maintaining a good work-life balance.

As mentioned above, it’s important to take into consideration some factors when deciding whether to use XP – if a team isn’t in a highly adaptive development environment, chances are that XP isn’t the best methodology to use. Furthermore, the client being always on-site is a slightly unrealistic and far-fetched requirement.

## 4.4 Lean

Researching into the roots of Lean, one would find many similarities when comparing it to Kanban – the main principle of Lean is to achieve the best business goal and delighting clients at the highest standard while reducing waste. However, this is where things get a bit tricky: Lean is more easily compared to Agile rather than being compared to any of the other methodologies. This is because Lean has its own set of rules and philosophy which highly differs from Agile. According to some studies mentioned in the Background Research, many believe that Agile was derived from Lean, making Lean an umbrella to all these methodologies above mentioned. Regardless, for this project and to ease the comparison between methodologies, Lean will be considered a methodology on the same ground of Scrum, Kanban, XP and Crystal. Although similar to Kanban, the practices of Lean are as it follows:
1.	Eliminating waste
2.	Learning amplification
3.	Decide as late as possible and Decide as fast as possible
4.	Team empowerment
5.	Integrity building
6.	Seeing the whole picture


  While examining the main differences between Lean and Agile, it was found that many of the aspects of Agile were derived from Lean, while still being almost like night and day. Where Agile wants to “execute tasks quicker while adapting to changes” and “making the development of processes flexible”, Lean on the other hand is all about “smart development where every aspect that does not bring value to the client is eliminated” and “making the development of processes sustainable” (Source: www.toptal.com/project-managers/Agile/project-management-blueprint-part-1-Agile-scrum-kanban-lean). Thus, while Agile was initially developed for Software Development, Lean was instead used for manufacturing in factories and overall industry work. 

## 4.5 Crystal


  If all the methodologies above mentioned are known to have a lot of documentation available to help implement its framework in a workplace, then Crystal would be on the opposite end of that spectrum. This is because Crystal is and Agile software development methodology that focuses primarily on people and their interactions while they work on a certain software. Whereas other Agile methods focus on the tools and techniques of development, Crystal’s focus is to keep people and its processes at the centre of the development processes. In its manifesto, “Crystal is a family of human-powered, adaptive, ultra-light, stretch-to-fit software development methodologies” (Source: http://blog.scrumstudy.com/what-is-crystal/) . The main principles of Crystal are:
1.	An incremental development approach: similar to Scrum’s sprints, projects using Crystal’s methodology are usually developed in timed iterations, with the product that was delivered at the end of this iteration is then implemented.
2.	Users are active in the project’s development: users are constantly informed of the progress of the project, 
3.	Commitments are delivered: focus is on a frequent delivery to make ensure the values of pleasing the client are up to standard. 

Since Crystal doesn’t have any set of prescribed techniques or tools, it is probably the most adaptable methodology that is covered on this report. Hence, the processes and tools are instead adjusted to the requirements of the project at hand. As previously mentioned, Crystal is also known as the “lightweight methodology” – as little to no documentation is available, teams instead focus towards “human-powered” resources such as open communication and a transparent flow of data between the stakeholders and team members.

## 4.6 Agile Picker

  For this project’s development, after a rigorous research into every methodology, what defined each one and a brief talk with my supervisor, it was found that the best methodology for this type of project would also be Agile methodology – in specific, Scrum. The reason why Scrum would be the most adequate for this type of project is the fact that, at the beginning of this project’s development, requirements weren’t completely well defined and were changing throughout the project’s implementation. Although development began in June 2018, research into the Agile Picker only began in late December, meaning that there would be no way I would plan to do so that early in the project’s lifecycle. One of the benefits though, is that I could contribute small releases throughout the Final Year Project’s module and feel as if I was doing good progress for the ultimate goal, which would be having a finalized web application.
	For this goal, I kept track of all the commits I made to Git and saw those as checkpoints, adding them to a Gantt Chart I created early on when I first started creating the project. What this also meant was that as I was researching into the different methodologies, I could be writing some Final Year Report sections alongside the code development, as most of the questions that were added into the code came directly from specific Agile principles from each methodology. 


# 5. Design

  Whenever a big scale project is being developed, its design is always important, if not the most important. One of the issues regarding this project’s design was how to convey that the right choices were being relayed back to the User. Not only that, it was important for me to create a tool that would reflect the amount of research that was put into each Methodology. A big source of inspiration was taken from the 2007’s computer game “Akinator”, that lets the User think of any character, imaginary or not, and through a series of Yes/No/Probably/Probably Not/Don’t Know, the AI behind the game always guesses it under 25 questions. Should the game not guess the character the User was thinking, it would prompt the User to input the character’s name to expand its Database. Although this Project wouldn’t match the amount of effort that was put into Akinator’s development and design, it was important for this Project’s design to match Akinator’s decision making and thought process. Obviously, a real AI isn’t behind Akinator’s success, nor was an AI implemented into the Agile Picker decision making, but only a basic simulation of a Reactive Artificial Intelligence. This means that it lets the User think that an intelligent entity is behind the decision process of an Agile Methodology, whereas instead it is simply achieved by a series of if statements and a scoring system. 
Regarding the User Interface, it was attempted to make it as basic as possible, to avoid User confusion as to where each section of the code was. As you can see below, the design was inspired by Facebook’s old design, by having a dashboard on the left with every section the User can access.

  The Profile was also a section in which extra care was taken to not overload the User with information. By keeping it relatively simple, the focus is on the User’s tasks rather than “making the profile look good”. Social elements would be added later on in the project’s development should the project be implemented on a dedicated server – the user would be able to have the ability to have a network of colleagues specific to each person rather than it being limited by the team you’re currently in, incentivizing collaboration on projects from people interested in the same methodology as you are. 

  The Teams section was an addition to the code that demonstrated how easy it would be to create a Team using a specific methodology, although it would need some extra development to make sure it would be usable in a dedicated server environment. Right now, team can only be added via a manual insertion into the database, rather than letting the User create Teams on the go. 

  The Database Administration also proved to be relatively easy, using Django’s built-in administration tools. As you can see, it’s very simple to manage the Database from the web app itself, allowing the creation of models on the fly with little extra effort – although the models have to be defined manually, as it will be discussed in the Implementation section, Django handles all the database creation of the models.

  The main focus of the Project’s design however, was the Agile Picker. Taking inspiration from Akinator, questions were presented to the User in a sequential way, and the following question would be presented depending on the answer the User gave from the previous questions. Furthermore, depending on the type of question, points would be awarded to each of the methodologies that were discussed previously.
 
  After answering the first question, a scoreboard will be displayed underneath the questions, showcasing how many points each methodology has, keeping in mind that regardless of how many points per methodology, it doesn’t mean that the highest point methodology will be the one suggested – per logic, the application will only suggest a methodology, advising the User depending on its answers. The points however, are only there to show if there’s other methodologies the User might be leaning to. Depending on the answers given by the User, the application then suggests a methodology that the User can and (following the project’s logic) should use in their next project’s development.

  All of the above code was implemented through Pycharm, and such code was then exported to a private GitLab repository that will, following this Project’s deadline, be made public and should it receive positive feedback, will be taken into further development and exported to a dedicated server where it will be made publicly available.


















# 6. Tools and implementation
## 6.1 Tools 

  As was mentioned in the review of tools and techniques, all the code was written in Django, which is a mix of HTML and Python, using PyCharm as an IDE. Furthermore, for testing and to make sure the GUI was properly developed, Python’s local server deployment proved to be essential for this purpose – this meant that the application wouldn’t need to be deployed to a public server at this point in time but, as previously discussed, should the app succeed in its implementation, it will be taken into consideration developing the application further into a free, online app that can be used by Users that have a sparking interest in the Agile Methodologies. For version control and to save the code on a cloud, a private Git repository was also set up under my personal account where all the commits and pushes were sent to. Under that repository, I’ve added both my home computer and laptop as trusted sources to commit – that way coding became possible both at home and at University. Git was not only used because the Version Control aspect of it really appealed to the overall mentality of this project development, but also for the usefulness of the information provided by Git for the completion of the Gantt chart – this way it was possible to get the exact dates some segments of code were pushed. Having never user Git before, I found that I should have been using it since the first year of University, as it proved essential for my future coding project endeavours.
	Also, this project was the first real coding project I’ve developed that I didn’t use SQL. Through Django’s built in sqlite3 database, managing the database using PyCharm made it so much easier than having to create a MySQL database on the side and then connecting it to the code. Further diagrams were made via draw.io’s free diagram creation application, which aided with the creation of the question tree used for the Agile Picker.

## 6.2.	 Implementation 

  The main aspect of this project and its goal is to help the user decide what the best Agile methodology is for a specific project – part of the challenge was to design code that made the user feel like its decisions were being taken into consideration when picking an Agile methodology. Obviously, an AI would be perfect for the implementation of this project, as it could learn the specifics of each Methodology and then discuss with the User what the best one would be – unfortunately, developing an AI from scratch wasn’t deemed feasible for this project’s scope. 

  The solution that was deemed the best for this problem was to code a “scoring” system that would award points to each methodology based on the user’s answer: this would mean there is never a clear path of questions that would lead to a specific methodology but also, splitting the questions into relevant groups, making it so that a User that answers “Yes” to Scrum questions will get queries regarding Kanban and Extreme Programming, but not many Lean or Crystal questions. In fact, one of the biggest challenges was researching into every methodology to find out what was it that distinguished each one from each other. For example, a question such as “Will your team work in sprints?” will mainly award points to Scrum, Kanban and Extreme Programming, whereas a question such as “Is your work mainly customer service related?” will award points to only Lean. For this purpose, a question tree was created in order to aid with programming and for visibility purposes.

  Firstly however, was to create the website in which the app would reside. As previously mentioned, Django was chosen to be the main programming language that was going to be used for this project. As a learning opportunity, I created from scratch a registering and login system using Django’s built-in Form library. For the main aspect of this app (being the Agile Methodology picker), perhaps a login or registering system wouldn’t be fully necessary. However, when this project was being coded, the intention for it was to implement as much as possible into the Project so that in the future, should this prototype be escalated into a fully-fledged web app, most of the work was already done. For the registering system, only the First and Last name were asked, as well as a Username and Password. These were all stored under Django’s modelling system, which is the same as database, using sqlite3. Although this database isn’t recommended for use in a large-scale web app with lots of data requiring to be saved, it worked perfectly for this small-scale prototype – the only data that is being saved is the login details of every registered user, as well as Tasks that the User might add in his profile. As you can see in the code below, Django handles the form processing automatically, saving it onto the “User” model that is used to store all the information about the login details.

    class Registration(UserCreationForm):
        email = forms.EmailField(required=True)

        class Meta:
            model = User
            fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

        def save(self, commit=True):
            user = super(Registration, self).save(commit=False)
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']
            user.email = self.cleaned_data['email']

            if commit:
                user.save()

            return user


  For other models however, these had to be coded manually, almost like the SQL that was learnt back in the first year of university. 

    class Profile(models.Model):

        created = models.DateTimeField(auto_now_add=True, editable=False)
        user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
        name = models.CharField(max_length=100, default='')
        bio = models.CharField(max_length=100, default='')
        jobtitle = models.CharField(max_length=100, default='')
        dob = models.DateField(("Date"), default=datetime.date.today)
        age = models.IntegerField(default=0)
        completedtasks = models.IntegerField(default=0)
        profilepic = models.ImageField(upload_to='profile_image', blank=True)
        team = models.ForeignKey(Teams, related_name='team_user_set', default=None, blank=True, null=True,
                                 on_delete=models.CASCADE)
        def __str__(self):
            return self.name

        class Meta:
            verbose_name = 'Profile'
            verbose_name_plural = 'Profiles'

        def create_profile(sender, **kwargs):
            if kwargs['created']:
                profile = Profile.objects.create(user=kwargs['instance'], name=kwargs['instance'],bio="This is your Bio.",
                                                 jobtitle="This is your Job Title.", dob=date.today(),
                                                 profilepic='profile_image/default.png')

        def calculate_age(self, dob):
            today = date.today()
            self.age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

        post_save.connect(create_profile, sender=User)

  The “Profiles” model pictured above was written by myself, and Django creates the model based on the requirements that I have specified. For example, the OneToOneField mentioned in the “user” line is key to specify that each user has only one profile. This was done to avoid duplicate Profiles being created to Users with the same first name, for example. Furthermore, a way had to be created as well to make sure the user could edit the profile post creation. To explain each object clearly:

•	created is an automatic Django feature that allows storage of when said object was created.
•	user is a one-to-one relationship, creating one Profile per User (for this implementation, only one profile is allowed per user).
•	def create_profile is a function in the database that is called whenever a User registers using my web application, or when changes are made to its profile. One of the learning opportunities in this case was figuring out how to edit a model object once it was already created through a form, meaning no manual intervention from an administrator would be needed

 Thus, the following code was written:

    class EditProfile(ModelForm):

        class Meta:
            model = Profile

            fields = (
                'bio', 'jobtitle', 'dob', 'profilepic'
            )
            labels = {
                'bio': 'Your Bio',
                'jobtitle': 'Your Job Title',
                'dob': 'Date of Birth',
                'profilepic': 'Profile Picture'
            }

        def save(self, commit=True):
            profile = super(EditProfile, self).save(commit=False)
            profile.bio = self.cleaned_data['bio']
            profile.jobtitle = self.cleaned_data['jobtitle']
            profile.dob = self.cleaned_data['dob']
            profile.profilepic = self.cleaned_data['profilepic']

            today = date.today()
            profile.age = today.year - profile.dob.year - ((today.month, today.day) < (profile.dob.month, profile.dob.day))

            if commit:
                profile.save()

            return profile

  This was made by using Django’s powerful form system, which would let me override the previous form that was created for the registration and replace it with this current one, although maintaining the super keys such as “User”.
	I chose to add a “Teams” object to the database, so that the User could create a team with a specific Methodology, and an object to keep track of the scoring system discussed previously per user. This way, a User can always review past choices for a specific methodology picker “session”. 
	 
  In the User’s profile, a Task Manager was created in order to let the User plan Stories, similar to what most Agile Planning tools offer in their respective apps – this was made by allowing the user to input a Story Value (0-100) and a Story Name (short description of the story), and, by pressing create, calling a function postStory() that will send an ajax request to the views.py page of Django (where method handling to the database is), sending both an action “create” (that, in the views.py page, distinguishes it from other ajax requests), the user that sent this request, it’s profile, the task (which as the .val() of the input #titletext), and the points of the task (.val() of the input #pointstext). Should the ajax return successfully, the Tasks <div> will then refresh on the .html page, giving the impression to the user that the page is being reactive. Should an error occur, the website will then display an error message. As you can see on the second code snippet, as the action that was sent via the function on the html page was “create”, the views.py will then call the model Tasks and create a new object with the values that were previously parsed – this way is how every single database object creation is made using Django’s framework.
 
    function postStory() {
        $.ajax({

            url: '/home/profile/',
            dataType: 'text',
            type: 'post',
            contentType: 'application/x-www-form-urlencoded',
            data: dict = {
                action: "create",
                user: "{{ user }}",
                profile: "{{ user.get_full_name }}",
                task: $('#titletext').val(),
                points: $('#pointstext').val()
            },
            success: function () {
                $('#to_do').load(document.URL + ' #to_do');
                $('#completed').load(document.URL + ' #completed');
            },
            error: function (jqXhr, textStatus, errorThrown) {
                alert("Oh No!");
                console.log(errorThrown);
            }

        });
    }

    if action == 'create':
        Tasks.objects.create(profile=p['profile'], username=p['user'], task=p['task'], type="todo", points=p['points'])
        return render(request, 'home/profile.html')

  One of the challenges to create this however, was to make the Tasks specific to the User, while adding a functionality for future development where, for example, another User would be able to search another User’s Profile and still see his Tasks. Although this involved a lot of research, it proved helpful for my future web application developments, as it was solved by a single line of code:
 
    url(r'profile/(?P<username>[a-zA-Z0-9]+)$', views.get_user_profile),

  Instead of having a static Profile .html, like I had in the beginning of this project’s development, I made the URL that led to each user’s profile depend on what username was being inserted into that URL.
  Most of the code however, was developed in short sprints, meaning I would develop a small feature each time I focused on programming, continuously developing incremental amounts that would eventually add up. The Agile picker for example, was developed throughout the Project’s lifecycle, as I would alternate between adding code to it and researching into each methodology. This meant that some questions that were initially chosen were later removed, as further research determined some Methodologies to share the same aspects, thus making questions for each one easier to pick. This was all programmed in a series of if statements, and depending on the User’s answer, it would attribute a certain amount of points for each methodology. For example, a question under the Scrum’s question line would always add points to the “Scrum meter”, but some questions were very similar to Kanban or XP, so in those cases points were added to all 3 but adding a few extra for Scrum. This was made to make the User feel like there wasn’t a single option for a methodology to pick, but rather the User (or in some cases, the team) had to come up with their own version of a methodology. The main implementation aspect of the code was to develop from scratch an Agile Picker that would simulate intelligent decisions based on the User’s input. Like it was discussed previously, the code was based on the question tree that was developed after a thorough research of each methodology. To translate this onto code, several blocks of questions were created in groups depending on what methodology they belonged to.
  
    <div id="scrum1" class="col-md-12 blue-section" style="color: whitesmoke; font-size: 18px; text-align: center">
        <br>Do requirements change monthly?<br><br>
        <button id="scrumyes" type="submit" class="btn btn-success btn-lg bouncy" onclick="Qscrum1()">Yes</button>
        <button id="scrumno" type="submit" class="btn btn-danger btn-lg bouncy" onclick="Qlean1()"
                style="animation-delay:0.07s">No
        </button>
    </div>
    
  This question block is placed in a <div> that has all of the scrum questions – furthermore, all scrum questions will have the same design as this one, only differing in the id (each question will have an ID composed of (Agile methodology + question number)) and the onClick function that Yes / No calls. For example, for this question, answering Yes would call a Qscrum1() function:
  
    function Qscrum1() {
        scrumpoints++;
        $('#scrum1').slideToggle("slow");
        $('#scrum2').slideToggle("slow");
    }
    
  For each function, points will always be assigned to the correct methodology, followed by performing a .slideToggle (JQuery pre-defined function to slide HTML elements in and out of view) on the question that the User just defined and ending with showing the following question (taking into consideration our question tree). Should the user vote No, a Qlean1() function would be called instead:
  
    function Qlean1() {
        leanpoints++;
        $('#scrum1').slideToggle("slow");
        $('#lean1').slideToggle("slow");

    }
    
  This time around, points are awarded instead to the lean methodology (since the User voted no) and following our question tree, the next question in line would be a lean one, so that question is then .slideToggled into view, so that the user can vote Yes or No. Once the User has answered all the questions, depending on which question line the User is, he will then be presented with an advised methodology. Let’s assume in this case, the methodology that was suggested was Scrum:
  
    <div id="scrumfinal" class="col-md-12 blue-section" style="color: whitesmoke; font-size: 18px; text-align: center; display: none;">
        <h2 style="color: white">Scrum</h2><hr>
        </div>
    <div id="pointsfinal" class="col-md-12 yellow-section"
         style="color: whitesmoke; font-size: 18px; text-align: center; display: none;">
        <p>Scrum Points: <span id="scrumpoints"></span>&nbsp;&nbsp;&nbsp;•&nbsp;&nbsp;&nbsp;Kanban Points: <span
                id="kanbanpoints"></span>&nbsp;&nbsp;&nbsp;•&nbsp;&nbsp;&nbsp;Lean Points: <span
                id="leanpoints"></span>&nbsp;&nbsp;&nbsp;•&nbsp;&nbsp;&nbsp;XP Points: <span
                id="xppoints"></span>&nbsp;&nbsp;&nbsp;•&nbsp;&nbsp;&nbsp;Crystal Points: <span
                id="crystalpoints"></span></p>
    </div>
    
  Both of these <div> will be presented to the User, one of them displaying the suggested methodology (this one will vary depending on which methodology is suggested), and another one that is always being displayed to the user, showcasing the amount of points per methodology. Although with this logic, there is only a finite number of possibilities that could derive from the User’s answers – to elevate this logic further, a higher number of questions would be necessary to fully understand the User’s intent and what the best methodology should be. However, the main objective of this project was to create a prototype to show that indeed, it is possible to guide a user in the right direction of picking an Agile methodology through a series of queries and a scoring system, and for that it succeeds. Through simple questions, this application could identify the areas in which the User, while picking a methodology, would more suitable to invest in. The way it is coded however, leaves plenty of space for the easy addition of more questions and more methodologies – the way the database is setup for this project incentivises further development into this Agile Picker.

  “ScrumEz”, being the main app of the Django that was created initially (Django requires an application to be created in the project’s folder before development starts) and “home” being the app where all HTML templates were created. Inside “ScrumEz” resided all the Django settings for the entire project, from the connection Hosts that were allowed, the external apps that were installed and required for the project to run, the code that made the connection between databases, password vaults and the static URL’s, for example. Inside “home”, however, was where all the HTML templates resided, python files that managed most of the back-end operations as well as database migrations data and a static folder. The reason between this well-defined separation was the logic behind the way this project was developed – the only aspect that would be changing drastically over the course of its life-cycle would be the HTML templates inside the “home” app and the Python files. Indeed, the way Django works provides an easy way to make drastic changes to, for example, the database, without affecting the rest of the code should any errors occur. This meant that the “ScrumEz” app could be used as the “terrain” to build the rest of the apps upon – this also means that in the future, like mentioned previously, it will be quite easy to add some extra Agile planning apps that have already been developed by me onto this “Umbrella” application in the making. 



# 7. Testing

## 7.1 Functional testing 

  Firstly, the difference between black box testing and white box testing has to be clarified – black box testing (sometimes known as behavioural testing) is when the structure of the program or the code is hidden from the person that is testing the project. This means that a User who might test a project using black box testing will not take into consideration the code’s structure. One of the main advantages of this type of testing method, amongst others, is that the testing can be made by someone else other than the developer, meaning that a developer-biased testing is avoided. This also means that testing can occur as soon as the project’s specifications are completed, which in this project’s case was very early on. White box testing, however, is when the tester has access to the code and to the structure of the project – in other words, it’s a test usually performed by the developer or someone who has access to the implementation of the code. One of the advantages of this is the fact that testing can be performed very early on in the project’s development, as most of the testing is performed internally and directly onto the code, not needing a GUI (or, in this project’s case, the web application fully developed, as front-end developing usually takes longer to perfect).

  Because of the nature of my project, most of the testing was conducted using a black box method – most of the test results that were important for the improvement of my code were whether the project suggested an adequate methodology to any user. Furthermore, since some of the Users testing my project have no knowledge of programming, it would be unfair to base my test results on an unfair testing circle. Also, under the context of my project and the way it is coded, it is relatively easy to add / modify current questions in the Agile Picker, so white box testing wasn’t used for a structural test on the project – as it will be mentioned in the next section, it wouldn’t make sense to use loop testing or condition testing on an app that is built around the feedback it gives the User, not how the User can interact with it.  However, an awareness of the disadvantages of black box testing have to be taken into consideration when comparing both. It is known that although behavioural testing is done from a user’s point of view, should the project’s specifications not be made available to the tester, it will be difficult perform test cases on the project. Furthermore, as black box testing was performed by Users other than myself, I as the developer, had the responsibility to perform white box testing on pieces of code I knew weren’t as refined. For this, I took practices of Extreme Programming which were discussed earlier on this report and performed some pair programming with a colleague that I have worked on several coding endeavours before. As they had more experience than me in Python development, I found that some of my methods needed rewriting to be more efficient, speeding up some database object handling.


## 7.2 User testing 

  As the Agile Picker that was developed was constructed around research performed on Agile Methodologies, it helped that while this project was being developed, the company where I was working at the time had just implemented an Agile Way of Working throughout its organisation. This meant that the application could be developed alongside colleagues that were learning Agile – this turned out to be greatly beneficial, as I could get constant feedback from both software development professionals as well as people who had no prior knowledge to Agile. Most of the tests that were conducted under these situations were Usability Tests – this meant that I had to serve as a moderator while I had multiple users come and test my application, attempting to get relevant feedback between tests.

  From my first initial round of tests (January 2019), the Agile Picker was starting to reach its final stage. As my supervisor advised, getting feedback from software developers that were used to Agile methodologies was key to make sure my project would be relevant in its final form. One of the first initial rounds of feedback was that there were not many questions, and the ones that I had were too specific – this resulted in two very distinct groups of people who tested my application: those that knew what the questions meant and to what methodology they would lead to, and those that thought the questions were too technical and didn’t mean much. For a while I thought the best solution would be to resort to a testing procedure called A/B testing, where I developed two distinct applications tailored for each one of those groups previously mentioned: one with very technical questions, such as “Will your team work in Sprints?” or “Will the Product Owner be available on-site?”, and one with very basic questions such as “Is the deadline for the project months away?” or “Is your team known for developing small bits of work with constant releases?”. This, however, proved mostly ineffective, as the projects aim was to help a User pick an Agile methodology, not to test the User’s knowledge on certain Agile topics. 
	However – there were two main tests that I wanted to conduct to ensure this app would make valid decisions for the Users. These were:
•	Agile Knowledge Test: User deciding on an Agile Methodology, then trying to answer the questions based on that previously decided methodology, and documenting whether or not the User got the same one – this would test whether the app’s questions were synchronous with a User’s knowledge of a methodology.
•	Blind Agile Knowledge Test: Users from different departments having no prior knowledge of an Agile Methodology answering the questions based on the requirements of their team, and documenting what Agile Methodology they got and compare it to what department they work in – this test would see if the application could, in fact, recommend an adequate methodology.

### 7.2.1 Agile Knowledge Test

•	Out of the 17 Users that guessed the methodology correctly:
o	12 were users that worked in a Scrum team and attempted to guess Scrum;
o	5 were users that worked in a Kanban team and guessed both Scrum and Kanban;
o	1 was a Scrum user with knowledge of XP’s framework and guessed XP;
Interestingly enough, the 3 users that did not guess the methodology correctly were also Scrum users, but instead ended up on the Lean question line. This was because one of the questions was poorly constructed, leading the user to a completely different question line based on a wrong answer. This was corrected afterwards and moved to another question line, leaving Scrum, Kanban and XP separate from Lean and Crystal. It is also interesting to note that most of the 20 Users that were involved in testing had any relevant knowledge to Lean or Crystal – while they might have heard the name before, knowledge was very basic.



### 7.2.1 Blind Agile Knowledge Test

  As most of the Users that participated in this test were people from outside the IT department, it’s interesting to note that the most widely picked methodology was Lean – a methodology that according to my research was mostly inclined towards customer service areas and was easily adaptable and integrated into any team. Scrum came in at a close second place, although this can easily be explained by the fact Scrum is the most widely used methodology in the other departments these tests were conducted. It is also interesting to note that although Crystal is the methodology that seems to be the most flexible when adapting to new projects, being a lightweight methodology and focusing mostly on people, only 3 people ended up on that question line that eventually led to Crystal – after this test, some Crystal questions were tweaked slightly to make them more approachable and to convey better the principles that define this methodology.


# 8. Conclusions and reflections

  The rise of Agile working in organisations can offer many benefits such as improved productivity and better team working. However, it is also often poorly understood, making it difficult to implement and maintain in a large organisation. This can be due to a lack of data when implementing an Agile Framework in a project’s development, mostly due to an inadequate spreading of information when it comes to what makes the Agile way of working different. From a questionnaire conducted between two groups of people – software engineers who were used to using Agile on a day to day basic and workers from other departments that have just recently been exposed to the Agile way of working, it was clear that the misinformation about Agile affected both groups of people. This, combined with a lack of resources online for the aid of a proper implementation of the Agile way of working, led to what I believe was a major issue.

  This project was developed to both improve the understanding of what Agile is and how it works, and to enhance the development process by providing a tool to plan the process and foster greater team collaboration. The main feature of the application was the tool to select the most appropriate methodology to use, making it unique amongst other existing Agile planning services. This was done by firstly researching into each Agile Methodology selected for this project: Scrum, Kanban, Extreme Programming, Lean and Crystal. What began as identifying the differences between methodologies, quickly became a what similarities existed between them – by realising how similar they were in some aspects, a question tree was then developed with questions being formulated around key aspects of each methodology while keeping a familiar, Agile feel to them. That being said, one of the biggest challenges was exactly this: as no other applications exist right now that aid the choice of an Agile methodology, most of the work on this project was put into creating original questions that carried an Agile methodology principle that was broken down enough to make it seem like a simple, honest question. The purpose of this application was, after all, to aid a User, and I would not want this to be done by bombarding him/her with a lot of technical questions. 

  Once enough questions were made though, they were then organised into logic groups, that would eventually lead to one methodology. While the application was indeed suggesting a methodology to the User, it felt too black and white, lacking diversity in suggestions and seeming like the previous answers wouldn’t matter, but only the last one that would lead to a correct methodology. Following this, a scoring system was promptly developed that, although one or two methodologies were still being suggested at the User, he/she could now see if there were other ones their project could use. This allowed for a feeling of “there’s not only one correct option” when it comes to Agile that I felt was a massive issue when implementing Agile in a business. This was then all translated into a web application that allows Users to Login, create and customise a Profile with personal information and even Tasks, and use the Agile Picker app where they will be suggested one of the five methodologies researched, alongside a numerical score for the other methodologies. One of the main findings after a lot of research into projects already using some type of Agile was that following the methodology’s documentation religiously most of the times didn’t work – one massive example of this was the lack of success of Extreme Programming. While, in theory, it is the most efficient way of producing good, error-free, clean code, one of its main principles is that all of the rules must be followed exactly as they’re stated. Perhaps this is why methodologies such as Scrum, Kanban and Lean and today’s market leaders, as they offer teams much flexibility that can be easily adapted into any project.

  Of course, despite the overall success of achieving my desired aims in this project, there are limitations. There are many more subsets of Agile that could be incorporated into further iterations of the application, and with further usage and user feedback, the methodology selection process can become more accurate. A further limitation of the work is that it lacks the scale for full implementation in an organisation. Projects of this size often require considerably more resources than were available for this initial stage. With increased budget and manpower the tool could offer additional features such as taking in consideration user feedback from previous iterations of the Agile Picker, gradually learning what People mean when they answer specific questions, questions being picked from a database of questions at random, and then being presented to the User in a smarter way than just a sequential flow of questions, and a more sophisticated AI could be developed to use the previous inputs to refine the methodology selection process.

  Overall, I would say, despite this being a small scale, initial stage of what has the potential to be a much larger project, I am pleased with the final product. The application built is a high-quality product with a unique feature and has achieved all I hoped to when beginning development. The process itself was at times challenging and required me to learn new programming techniques, gain an in-depth knowledge of the subject matter, and apply myself in an, at times high-pressured, project of this scale for the first time. Despite this, the creation of a new tool for the growing area of Agile methodologies is, I believe, highly useful and presents many more exciting opportunities to expand the range of applications on offer to enhance its use and effectiveness. While in this case the product has been developed with large corporate software developers in mind, there is potential to adapt it for smaller teams, students, and even those without an IT background, bringing the Agile way of working to a whole new audience. 

	
 
# 9. References

Agile Alliance. (2019). What is Extreme Programming (XP)?. [online] Available at: https://www.Agilealliance.org/glossary/xp/#q=~(infinite~false~filters~(postType~(~'post~'aa_book~'aa_event_session~'aa_experience_report~'aa_glossary~'aa_research_paper~'aa_video)~tags~(~'xp))~searchTerm~'~sort~false~sortDirection~'asc~page~1) [Accessed 30 Apr. 2019].
AltexSoft. (2019). Extreme Programming: Values, Principles, and Practices. [online] Available at: https://www.altexsoft.com/blog/business/extreme-programming-values-principles-and-practices/ [Accessed 30 Apr. 2019].
Atlassian. (2019). What is a Kanban Board? | Atlassian. [online] Available at: https://www.atlassian.com/Agile/kanban/boards [Accessed 30 Apr. 2019].
Ben-David, A., Gelbard, R. and Milstein, I. (2012). Supplier ranking by multi-alternative proposal analysis for Agile projects. International Journal of Project Management, 30(6), pp.723-730.

Blog.scrumstudy.com. (2019). 6 Main Principles of Scrum Methodology | SCRUMstudy Blog. [online] Available at: http://blog.scrumstudy.com/6-main-principles-of-scrum-methodology/ [Accessed 30 Apr. 2019].
Conboy, K., Coyle, S., Wang, X. and Pikkarainen, M. (2011). People over Process: Key Challenges in Agile Development. IEEE Software, 28(4), pp.48-57.
Cooke, J.L. (2012). Everything you want to know about agile, IT governance publishing
Dikert, K., Paasivaara, M. and Lassenius, C. (2016). Challenges and success factors for large-scale Agile transformations: A systematic literature review. Journal of Systems and Software, 119, pp.87-108. 

dzone.com. (2019). Agile Framework Comparison: Scrum vs Kanban vs Lean vs XP - DZone Agile. [online] Available at: https://dzone.com/articles/Agile-framework-comparison-scrum-vs-kanban-vs-lean [Accessed 30 Apr. 2019].
eBbiz Solutions, h. (2019). Methodologies | Design Thinking | Lean, Agile, SIT - Ebiz Solutions. [online] eBiz Solutions, LLC. Available at: https://www.thinkebiz.net/methodologies/ [Accessed 30 Apr. 2019].
Everyday Kanban. (2019). What is Kanban?. [online] Available at: http://www.everydaykanban.com/what-is-kanban/ [Accessed 30 Apr. 2019].
gadade, s., sri, s., Fan, #., Choudhary, S. and kinsbriner, E. (2018). Web Application Testing Complete Guide (How to Test a Website). [online] Softwaretestinghelp.com. Available at: https://www.softwaretestinghelp.com/web-application-testing/ [Accessed 2 Nov. 2018]. 

Ghezzi, A. and Cavallo, A. (2018). Agile Business Model Innovation in Digital Entrepreneurship: Lean Startup Approaches. Journal of Business Research. 

Graphic Products. (2019). What Is the Lean Process?. [online] Available at: https://www.graphicproducts.com/articles/lean-process/ [Accessed 30 Apr. 2019].
Hoeren, T. and Pinelli, S. (2018). Agile programming – Introduction and current legal challenges. Computer Law & Security Review, 34(5), pp.1131-1138. 

Hseih, J.J.P-A., Zmud, R. (2006) Understanding post-adoptive usage behaviours: a two-Dimensional view, Presented at the meeting of the DIGITWorkshop, Milwaukee, Wisconsin, USA.

Javdani Gandomani, T. and Ziaei Nafchi, M. (2016). Agile transition and adoption human-related challenges and issues: A Grounded Theory approach. Computers in Human Behavior, 62, pp.257-266. 

LLC, O. (2019). Agile Framework Comparison: Scrum vs Kanban vs Lean vs XP - ObjectStyle.com. [online] Objectstyle.com. Available at: https://www.objectstyle.com/Agile/Agile-scrum-kanban-lean-xp-comparison [Accessed 30 Apr. 2019].
Masood, Z., Hoda, R. and Blincoe, K. (2018). Adapting Agile practices in university contexts. Journal of Systems and Software, 144, pp.501-510. 
MiroBlog | A blog by Miro. (2019). How to choose between Agile and Lean, Scrum and Kanban — which methodology is the best?. [online] Available at: https://miro.com/blog/choose-between-Agile-lean-scrum-kanban/ [Accessed 30 Apr. 2019].
Newline.tech. (2019). Crystal Clear Methodology. [online] Available at: https://newline.tech/blog/crystal-clear-methodology/ [Accessed 30 Apr. 2019].
Number8. (2019). Kanban Versus Scrum in Agile Methodology | Blog - Number8. [online] Available at: https://number8.com/kanban-versus-scrum/ [Accessed 28 Jan. 2019].
Papatheocharous, E. and Andreou, A. (2014). Empirical evidence and state of practice of software Agile teams. Journal of Software: Evolution and Process, 26(9), pp.855-866. 

Patanakul, P. and Rufo-McCarron, R. (2018). Transitioning to Agile software development: Lessons learned from a government-contracted program. The Journal of High Technology Management Research. 

Planitpoker.com. (2019). PlanITpoker: Online Scrum planning poker for Agile project teams. [online] Available at: https://www.planitpoker.com [Accessed 12 Jan. 2019].
Powell-Morse, A. (2019). Extreme Programming: What Is It And How Do You Use It?. [online] Airbrake Blog. Available at: https://airbrake.io/blog/sdlc/extreme-programming [Accessed 30 Apr. 2019].
Powell-Morse, A. (2019). Waterfall Model: What Is It and When Should You Use It?. [online] Airbrake Blog. Available at: https://airbrake.io/blog/sdlc/waterfall-model [Accessed 12 Jan. 2019].
Rasnacis, A. and Berzisa, S. (2017). Method for Adaptation and Implementation of Agile Project Management Methodology. Procedia Computer Science, 104, pp.43-50. 

Resources.collab.net. (2019). What Is Agile Methodology?. [online] Available at: https://resources.collab.net/Agile-101/Agile-methodologies [Accessed 28 Jan. 2019].
Rola, P., Kuchta, D. and Kopczyk, D. (2016). Conceptual model of working space for Agile (Scrum) project team. Journal of Systems and Software, 118, pp.49- 63. 

Saga, V.L., Zmud, R.W. (Eds.), (1994), The Nature and Determinants of IT Acceptance, Routinization, and Infusion. North-Holland, Amsterdam. 

Scrum.org. (2018). What is Scrum?. [online] Available at: https://www.scrum.org/resources/what-is-scrum [Accessed 5 Nov. 2018]. 
Smartsheet. (2019). What's the Difference? Agile vs Scrum vs Waterfall vs Kanban. [online] Available at: https://www.smartsheet.com/Agile-vs-scrum-vs-waterfall-vs-kanban [Accessed 30 Apr. 2019].
Software Testing Fundamentals. (2019). Black Box Testing - Software Testing Fundamentals. [online] Available at: http://softwaretestingfundamentals.com/black-box-testing/ [Accessed 30 Apr. 2019].
Software Testing Fundamentals. (2019). White Box Testing - Software Testing Fundamentals. [online] Available at: http://softwaretestingfundamentals.com/white-box-testing/ [Accessed 30 Apr. 2019].
Taiga - Love your projects. (2019). Taiga.io. [online] Available at: https://taiga.io [Accessed 28 Jan. 2019].
Tastycupcakes.org. (2019). TastyCupcakes.org – Fuel for Invention and Learning. [online] Available at: https://tastycupcakes.org [Accessed 30 Apr. 2019].
Younas, M., Ghani, I., Jawawi, D. and Khan, M. (2016). A Framework for Agile Development in Cloud Computing Environment. Journal of Internet Computing and Services, 17(5), pp.67-74















# 10. Bibliography

Atlassian. (2019). Jira | Issue & Project Tracking Software | Atlassian. [online] Available at: https://www.atlassian.com/software/jira [Accessed 30 Jan. 2019].
Djangoproject.com. (2019). The Web framework for perfectionists with deadlines | Django. [online] Available at: https://www.djangoproject.com [Accessed 30 Jan. 2019].
Docs.djangoproject.com. (2019). Django documentation | Django documentation | Django. [online] Available at: https://docs.djangoproject.com/en/2.1/ [Accessed 30 Jan. 2019].
G2 Crowd. (2019). PyCharm Reviews 2019 | G2 Crowd. [online] Available at: https://www.g2crowd.com/products/pycharm/reviews [Accessed 30 Jan. 2019].
JetBrains. (2019). PyCharm: the Python IDE for Professional Developers by JetBrains. [online] Available at: https://www.jetbrains.com/pycharm/ [Accessed 30 Jan. 2019].


 
