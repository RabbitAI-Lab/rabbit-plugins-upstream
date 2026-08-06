## Description: <br>
Manage CODESYS PLC recipes via iFA Evolution, including recipe conversion, cam data filling, and deployment-oriented file preparation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paudyyin](https://clawhub.ai/user/paudyyin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and automation engineers use this skill to convert iFA .txtrecipe files to CoDeSys text recipes, convert edited CoDeSys recipes back to iFA binary recipes, and fill cam displacement data from ProdData recipe files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated recipe files may be incorrect if the wrong source, output, or RecipeConfig.json path is selected. <br>
Mitigation: Run the scripts on copies of recipe directories, choose paths deliberately, and validate generated .txtrecipe files before importing them into PLC or production tooling. <br>
Risk: The skill performs local PLC recipe file conversion and writes output files that may later be used in production tooling. <br>
Mitigation: Install and run it only when working with iFA/CODESYS recipe files, and review outputs before deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/paudyyin/skills/ifa-codesys-recipe) <br>
- [Publisher profile](https://clawhub.ai/user/paudyyin) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with PowerShell command examples and generated recipe files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local .txt, .txtrecipe, and summary files through PowerShell scripts; users should validate generated recipe files before importing them into PLC or production tooling.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
