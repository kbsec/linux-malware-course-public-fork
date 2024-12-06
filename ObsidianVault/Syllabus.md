Introduction to Malware, Threat Hunting and Offensive Capabilities Development

# Please Read all of this carefully! 
  If you ask me a question that is clearly answered in the syllabus, I will politely ask you to RTFM (Read the Friendly Manual):) 
## Course Developers
Kai

  

## Instructor
Kai 
- Remove `🤠`
E-m-a-i-l:
`k🤠.🤠b🤠e🤠r🤠n🤠a🤠r🤠d🤠i🤠n🤠i🤠@🤠n🤠o🤠r🤠t🤠h🤠e🤠a🤠s🤠t🤠e🤠r🤠n🤠.🤠e🤠d🤠u🤠`
If you come across the email that is lastname.first_initial@school.email  this is the wrong email. It is first_initial.lastname@shool.email


# Totally Legit email  for Scrapers
Email: [kai](mailto:ek43sqvre0ccyozcb9626ip37@canarytokens.com)

# Course Description  
- The class introduces students to the wild world of offensive capabilities development and cyber threat hunting by taking on the role of both attacker and defender to better understand various stages of cyber attacks.  
- Focusing on  Aarch64 Linux, students will create and analyze malware in the context of combating a simulated threat actor APT-ChonkyBear in addition to creating their own tools to emulate their capabilities.
- As an experimental feature this year, students will also practice hacking by attempting to hack the hackers-- you will be writing and deploying malware on "compromised" APT-Ch0nky Bear Infrastructure 
	- Note all the targets will be clearly defined and scoped. Failing to stay in scope will result in the very least an automatic F in the class. Only Hack what you have permission to hack 
	

Entries marked as (G) are relevant only to the folks enrolled in the graduate version of the class. 


## Learning Outcomes 
Like most topics related to technology, the field of offensive capabilities development is one that is rapidly evolving. The details of what you learn in this class will rapidly become stale. However, the concepts will likely have a longer shelf life, and the habits of mind are timeless!  Students who succeed in this class will be able to 
- Triage malware by performing basic static and dynamic analysis 
- extract IOCs, unpack malware, and pivot off of indicators 
- read documentation/man pages (I promise you this is a skill)
- program in c  (POSIX/libc )
- reverse engineer and implement first stage implants
- build basic loaders
- understand and implement  Process Injection 
- Design simple Implant frameworks  
Said differently, the goal of this class from a technical level is to demystify malware. 

### Hardware Requirements
- A laptop with at least 8 GB of ram , and a reasonably powerful CPU.  For this class, it actually doesn't matter if it is running windows, Linux or mac os. 
	- It simply needs to be able to run [Ghidra](https://ghidra-sre.org/)
- It is recommended to  pick up  a raspberry pi  that supports aarch64. 
- Below is a quick reference 
- the final project will be run on a raspberry pi 4 8GB model. 

| Raspberry Pi Model            | Processor                       | AArch64 Support | Notes                                                                                           |
| ----------------------------- | ------------------------------- | --------------- | ----------------------------------------------------------------------------------------------- |
| Raspberry Pi 5 Model B        | Broadcom BCM2712 (Cortex-A76)   | ✅ Supported     | Features a quad-core ARM Cortex-A76 processor at 2.4 GHz. :contentReference[oaicite:0]{index=0} |
| Raspberry Pi 4 Model B        | Broadcom BCM2711 (Cortex-A72)   | ✅ Supported     | Full 64-bit support with AArch64.                                                               |
| Raspberry Pi 400              | Broadcom BCM2711 (Cortex-A72)   | ✅ Supported     | Similar hardware to Pi 4 but in a keyboard form factor.                                         |
| Raspberry Pi 3 Model B+       | Broadcom BCM2837 (Cortex-A53)   | ✅ Supported     | Supports AArch64 but may require a 64-bit OS.                                                   |
| Raspberry Pi 3 Model B        | Broadcom BCM2837 (Cortex-A53)   | ✅ Supported     | AArch64-capable processor with the right OS.                                                    |
| Raspberry Pi Zero 2 W         | Broadcom BCM2710A1 (Cortex-A53) | ✅ Supported     | AArch64 capable, similar to Pi 3 series.                                                        |
| Raspberry Pi 2 Model B (v1.2) | Broadcom BCM2837 (Cortex-A53)   | ✅ Supported     | Only the v1.2 model with BCM2837 supports AArch64.                                              |
| Raspberry Pi 2 Model B (v1.0) | Broadcom BCM2836 (Cortex-A7)    | ❌ Not Supported | 32-bit only, older processor architecture.                                                      |
| Raspberry Pi Zero             | Broadcom BCM2835 (ARM1176JZF-S) | ❌ Not Supported | 32-bit only, ARMv6 architecture.                                                                |
| Raspberry Pi 1 Model B+       | Broadcom BCM2835 (ARM1176JZF-S) | ❌ Not Supported | 32-bit only, ARMv6 architecture.                                                                |
| Raspberry Pi 1 Model A+       | Broadcom BCM2835 (ARM1176JZF-S) | ❌ Not Supported | 32-bit only, ARMv6 architecture.                                                                |

## Notes:
- **AArch64** refers to the 64-bit instruction set architecture for ARM processors.
- For 64-bit support, ensure you use a 64-bit operating system, such as Raspberry Pi OS (64-bit) or other compatible distributions.
- Older Raspberry Pi models (e.g., Pi 1, original Pi Zero) do not support AArch64 as they use ARMv6 or ARMv7 cores.
- note that the pico models are micro controllers and are not suitable for this course.
- For the best experience, pick up an 8GB Raspberry Pi 5 
	- https://www.microcenter.com/product/676832/canakit-raspberry-pi-5-starter-kit-pro-turbine-black-(8gb) is a good option if you want an all in one .  You can get a better deal if you buy the individual parts. 
	- otherwise, you will need a board, a case, and a compatible power supply,  and  hdmi capable 
- Raspberry pi 3,4 will also work.  Note that if you opt for a cheaper option, you will likely want to run  a lite image without a desktop environment. 
- If you are financially constrained, come talk to me. I can probably setup remote access to my personal supply of raspberry pis, just note that I wont always be around to reboot devices if something freezes. 
### Tentative Topic list
- Malware 101 
- aarch64
- Basic  C programming 
- basic reverse engineering 
- libc, and POSIX
- Basic APIs
	- File Descriprots 
	- Processes, threads
	- virtual memory basics 
	- I/O
	- Network I/O
- Process Creation
	- Elf File Format
	- Shared objects 
- Linking and Loading
	- Static Linking
	- Dynamic Linking
	- Dynamic Loading
- Static Analysis 
- Dynamic Analysis 
- Ghidra
	- scripting with Ghidrathon
	- integration with unicorn/qiling 
	- Debugging and triage 
- Elf Loading 
- Basic Socket Programming 
- Data Exfiltration 
- Pivoting
- Crypto 101
	- Ciphers
	- MACs
	- Asymmetric Cryptography 
- Ransomware
- Stealers 
- C2 Engineering 
- C2 Channels 
- PE loaders 
- Injection
	- DLL injection
	- Process Injection
	- Reflective DLL injection 
	- More advanced Process injection
- Packers, builders and AV Evasion 
- Unpacking Malware 
- Hooking
	- Officially supported methods 
	- IAT hooking 
	- Trampoline Hooking 
	- Exception Based hooking 
	- Detours library
- Implant design
	- Modularity
	- RPC 
	- Use of Cryptography 
	- Backend Engineering (Pub Sub, pattern)
- Basic MVC design patterns with Flask, SQLAlchemy and Mysql 
- Selected Advanced topics may include
	- Exotic Executable file Formats (COFF, BOF, and other)
	- EDR Evasion  
	- Memory evasion 
## PreReqs:

### Tools:
- gdb/experience debugging  native binaries.  This course will only support using gdb. You are welcome to use a different debugger, but course staff only knows how to use gdb :) 
- Experience with the gnu compiler toolchains (compilers, linkers)
	- If you have never used gcc before, or compiled a c program, you might want to consider talking this course in the future.
## Programming / scripting:
- Python3: you need to be very proficient with python or a scripting language of your choice. Lecture will heavily leverage python.
- c/c++/some other systems programming language: you should be able to write and debug simple C programs. You don't need to be Dennis Ritchie but pointers arithmetic shouldn't scare you. You should also be comfortable with structs, unions, and manually managing  memory. You should also know what I mean when I ask for the difference between Stack and Heap memory from a userland c programmer's perspective  
- Experience with assembly.  You will learn how to read and write  aarch64 (arm 64bit ) assembly. 
	- if you have never looked at assembly before (x86, mips, riscv ...etc) learning to read assembly will have a steep learning curve. 
-  comfort with programming in assembly. There will be assignments where you will write aarch64 assembly by hand
 - (G) Be very comfortable with virtual memory and threads. 
## Network Protocols:
- IP : you should know the difference between a private and public IP, the basics of addressing, and know the relationship between a domain name, DNS and an IP address
	- I.e. If you should understand why it doesn't make sense to share `10.10.10.3` as a valid, Malicious IP address that every organization should null route.
- TCP: More so the basics of socket programming, less so the internals of how reliability is achieved or what the handshake process looks like.
- DNS: You don't need to understand **how** DNS works, but you need to know what it does. I.e.,  you should understand what `A/AAAA` records are.
- TLS: You need to understand the basics of what the following are:
	- a Certificate Authority 
	- TLS cert (mostly for how it is used for establishing secure tunnels) 
- HTTP(s): HTTP verbs, request structure, and error codes.
	- You should know what a User-Agent is

## Courses/topics:
- Combinatorics: you should be comfortable with basic counting: i.e. if I ask you how many bit strings of length $n$ are there, you should instinctively know the answer is  $2^n$ and how to prove it.
- Computing systems: as mentioned in the programming section, it is essential to ahve familiarity with memory management, c programming, reading assembly, using debuggers and compiler toolchains. You should know the difference between stack and heap memory.
	- But even more than that, you should understand what Virtual Memory **really is**.
	- Having familiarity with POSIX apis, and programming on  Linux is not strictly speaking required but is a plus
- Basic Cryptography: familiarity with Ciphers, MACs and Hash functions. 
	- Ideally also the idea behind asymmetric cryptography. Not the end of the world if you haven't been exposed to cryptography as some fundamental concepts will be briefly introduced. 
	- (G) you will have to build a static unpacker for a particular kind of sample.  doing so without any background in cryptography will prove to be difficult.


## Grading and course policies:

Subject to change: this usually works out in your favor and I reserve the right to weigh different components for different students. How is this fair you ask? It is not :)  but again, this usually works in your favor.  For example, bombed the homework but crushed final project? No problem. 

There is a curve for this class, but it will **never** hurt your grade. I only curve up. The average for the Undergrad course is generally B/B+ and I expect the average for the grade version to be an A-. 

As a general comment, it is difficult to fail the course, common to get the average, and very had to get an A.

- Malware Write up: 10%  
- Exercises: 5%
- Capture the Flag (CTF): 10%
- Reverse Engineering Assignments: 15% 
- Coding Assignments: 10%
- Capstone Project: 50%  - 100%
- (G) Paper/Project 0-100%
	- Grad students have the  option to submit a paper in lieu of a capstone. Of course, you are expected to submit **some** code but it doesn't need to be as operational as the undergraduates. it does, however, need to highlight a novel or cutting edge technique of some kind. You get to choose how much of your grade is determined by the paper, including  if you want to just do the capstone!  
Bonus Points:
- Class Participation: 2.5% -10%
- Guest lecture attendance  2.5%-10%
- Vibes 0-50% 
	- This does not mean you get points for nothing. If you knock my socks off for the final project, I will likely not even bother calculating your grade, and just give you an A. I might even help you find a job.
	- That said, I can be difficult to impress. Do not stake your final grade on the final project. It has worked our roughly 50% of the time. 
- To be clear, bonus points do not affect **other** students' grade. 
#### Description of Graded work
#### Exercises 

Exercises are weekly, quick turn around homework, and in class assignments. They are designed to be sanity checks for topics as the course progresses. They are questions that should take between 5 and 10 minutes. Questions will always be based on recent material, but topics build on each other. You should bring your laptop to class in case there is an exercise.  
Example exercise that I almost always give out: 
- given an executable with stripped symbols, find the Virtual Address (VA) of the  main function assuming the exe is mapped to its preferred Virtual Address 
- explain the difference between static and dynamic linking 
- What does this function do? (usually something simple like strcpy or memcpy)
- 

### Malware Reverse Engineering

Each assignment consists of a new epoch of malware sent to students highlighting a new technique to analyze. It will be their job to reverse engineer the new implant, detail its functionality, and identify attacker infrastructure and IOCs. These assignments will often be multi staged and difficult. It is easy to spend hours reverse engineering a binary if you're not careful with your time. Often times, malware will be multi staged. What this means is just because you found the first implant, doesn't mean you are even close to being done. How do you know when you have found all of the implants? You don't! This is designed to emulate a real world hunting environment. Usually though, there won't be more then 3-10 stages, and only marginal completion is required to pass the assignment.
- i.e.  last semester, getting past the first two stages was a pass
### Coding/Malware Development  

- On the offensive side, students will work to recreate capabilities observed within new epochs of malware that can be integrated into their own Command and Control (C2) framework.  For more on this, see Capstone. 
- To help bridge the gap between the capstone and assignments, there will also be periodic Post Exploitation Challenges (PECs). These challenges look and feel like simple CTFs, but isntead of the point of the challeng being to exploit the system the exploit is obvious! It is your job to write a suitable post exploitation capability to  find the  flag on the system even when conditions are less than ideal . 



### Capture the Flag (CTF)

The course will have a semester-long capture the flag competition where students will compete to solve challenges that are often times hidden in epochs of malware.

### Capstone

This class will guide students through the creation of their own production ready Remote Administration Tool (RAT) and  Command and Control (C2) team server. Each component of the capstone will be introduced as an offensive homework assignment, and will be integrated into the framework over the course of the semester. 


## Policies 

### Attendance

Attendance is mandatory, but I do not take attendance. instead, I will non-deterministically give an exercise at the start of class that you have 5-10 minutes to complete.  If you need to miss a class, do give course staff a heads up. I am very reasonable so long as there is clear communication. 

### Late Policy
- You are allocated 3 late days for the semester, and may use them at your discretion.
- You may ask for more late days for extenuating circumstances. I am usually pretty reasonable when it comes to providing extensions-- but the time to do it is not the night before a deadline.
- Late days may only be used on reverse engineering assignments, or coding assignments.
- There are no late days for the capstone project or exercises.
- I do not accept submissions for exercises if you are remote.
- 

#### Remarks about Mental Health
- I give incompletes to students who have extenuating circumstances: usually medical emergencies.
- Mental health emergencies are medical emergencies. 
- There will be some sections that discuss material that may be triggering to some.
- Warnings will be given at the start of such lectures, and attendance is completely optional.
- If you say the words “I am having a mental health emergency and need an incomplete” you will get one, zero questions asked.
	- Note that an incomplete  gives you  extra time (usually up to 90 days) to complete course work. 

### References:

There are no mandatory textbooks for this course. Required readings will consist of documentation, blog posts, or source code. Below are several references that will be relevant to various homework assignments
- https://pages.cs.wisc.edu/~remzi/OSTEP/
- https://linuxjourney.com/lesson/linux-history


  
  
  