## Description: <br>
Interact with live Smalltalk image (Cuis or Squeak). Use for evaluating Smalltalk code, browsing classes, viewing method source, defining classes/methods, querying hierarchy and categories. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[johnmci](https://clawhub.ai/user/johnmci) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to work with live Squeak or Cuis images, including evaluating Smalltalk code, browsing classes and methods, editing definitions, auditing comments, and generating SUnit tests. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can run and persistently modify live Smalltalk images. <br>
Mitigation: Prefer playground mode for experiments, review define/delete/generate operations before use, and back up dev images before persistent work. <br>
Risk: LLM-powered explain, audit, and test-generation commands can send source code to configured external providers. <br>
Mitigation: Use those commands only with code the user is allowed to share and configure an approved provider and model. <br>
Risk: The skill relies on configured VM and image paths and a local daemon. <br>
Mitigation: Use trusted Squeak/Cuis VM and image paths, check daemon status, and stop the daemon when finished. <br>


## Reference(s): <br>
- [Squeak setup documentation](https://github.com/CorporateSmalltalkConsultingLtd/ClaudeSmalltalk/blob/main/SQUEAK-SETUP.md) <br>
- [Clawdbot setup documentation](https://github.com/CorporateSmalltalkConsultingLtd/ClaudeSmalltalk/blob/main/CLAWDBOT-SETUP.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [CLI text and Markdown with inline shell and Smalltalk code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May modify a live Smalltalk image; generated SUnit tests can be filed into the running image.] <br>

## Skill Version(s): <br>
1.7.0 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
