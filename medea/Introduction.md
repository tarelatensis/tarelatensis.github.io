**Seneca's Medea with minimal notes** 

Edited by [Thomas Arelatensis](https://tarelatensis.github.io/) (first online: 4 Jan 2026).

**Introduction**

This is the Latin text of Seneca's *Medea*, with enough Latin annotations to allow understanding by readers with only a moderate command of Latin. 

Simply put, the ideal outcome would be that a reader with basic knowledge of Latin \- say, someone who has gone through both volumes of Lingua Latina Per Se Illustrata, maybe a bit of Caesar, and who can easily read the Gesta Romanorum or the Vulgate \- should be able to read, understand, and hopefully enjoy the text of the play with only minimal effort.

To this end, as many annotations as were thought to be helpful in understanding the actual text were included \- but only those. In particular, only the strict minimum of mythological background that is absolutely necessary to follow the intrigue is reported. For example, the events of the quest for the Golden Fleece are mostly left aside; however, the fate of Hercules and King Pelia are quickly described, since several passages of the play assume knowledge of these events.

Accordingly, the Latin in the notes has been deliberately kept as simple as possible, with basic vocabulary and a syntax as close to that of modern European languages as reasonably feasible (and sometimes perhaps a bit beyond that). An occasional glimpse at the dictionary may still be required here and there.

An important consideration has been to avoid so-called "spoilers", both in the notes and the main text. For some reason, many editors routinely reveal future events when they explain a passage. This has been avoided as much as possible here. For example, while each scene is introduced by a quick description of the ongoing action, the actual outcome is left unstated.

**Text**

The basic text is entirely from [Frank Justus Miller's 1927 edition](https://www.google.com/books/edition/Seneca_s_Tragedies/S6pM-L1KuD8C) for the Loeb Classical Library. However, the punctuation has been altered in various places to facilitate comprehension.   
For interpreting and explaining the text, in addition to Miller's translation, [Johann Caspar Schroeder's 1728 edition](https://www.google.com/books/edition/L_Annaei_Senecae_Tragoediae/C4dZAAAAcAAJ) (with its many notes collated from various authors) was also consulted, as well as [Hugh MacMaster Kingery's 1896 edition](https://www.google.com/books/edition/The_Medea_of_Seneca/Bo1fAAAAMAAJ). Several of Thomas Farnaby's notes are also reproduced from Schroeder's collation, since they are both highly informative and remarkably clear.

In one passage ("meruere cuncti") the changes in punctuation slightly alter the meaning and accord with Schroeder's interpretation rather than Miller's.

Long vowels are indicated by a macron only when vowel length is semantically or grammatically informative. Thus, *manūs* is distinguished from *manus*, and *dea* from *deā*, but *quo* and *spiritu* are always written without macron.

In the notes, paraphrases longer than a single word are introduced by "i.e.", or by the term being paraphrased in italics. However, in many cases, the words are kept identical but merely re-ordered to facilitate comprehension (perhaps with some additional words for clarification); these reorderings are introduced by the equal sign "=", with any added words enclosed in square brackets "\[\]".

**Technical details**

The base working copy of this text is a [Google Docs](https://docs.google.com/document/d/11PLcpPvVMFMB53TMorVgOgm5aIXcb4RpEwhFkV4nvkM/edit?usp=sharing) document. This is exported as MarkDown, then converted into HTML with Pandoc (pandoc ./Medea.md \-o Medea.html \--preserve-tabs). The resulting HTML code is then processed by a Python script to apply the formatting expected by the Tufte CSS style sheet (python process.py \> Medea-processed.html), chosen both for its visual appearance and for its excellent handling of side notes. Since this website is hosted on GitHub, all necessary documents and scripts are included in the repository.

This edition is released under the Creative Commons 4.0 license with Attribution ([CC-BY](https://creativecommons.org/licenses/by/4.0/)).

**Links**

* Creative Commons 4.0 Attribution License (CC-BY): [https://creativecommons.org/licenses/by/4.0/](https://creativecommons.org/licenses/by/4.0/)   
* Frank Justus Miller, Seneca's Tragedies, Loeb edition, 1917: [https://www.google.com/books/edition/Seneca\_s\_Tragedies/S6pM-L1KuD8C](https://www.google.com/books/edition/Seneca_s_Tragedies/S6pM-L1KuD8C)   
* Johann Caspar Schoreder, L. Annaei Senecae Tragoediae, 1728: [https://www.google.com/books/edition/L\_Annaei\_Senecae\_Tragoediae/C4dZAAAAcAAJ](https://www.google.com/books/edition/L_Annaei_Senecae_Tragoediae/C4dZAAAAcAAJ)   
* Hugh MacMaster Kingery, The Medea of Seneca, 1896: [https://www.google.com/books/edition/The\_Medea\_of\_Seneca/Bo1fAAAAMAAJ](https://www.google.com/books/edition/The_Medea_of_Seneca/Bo1fAAAAMAAJ)   
* GitHub repository: https://github.com/tarelatensis/tarelatensis.github.io/tree/main/medea