## Description: <br>
Generate satirical "math slop" ragebait formulas that connect famous constants in trivially true but profound-looking equations and output LaTeX. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[0xmugen](https://clawhub.ai/user/0xmugen) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and external users can use this skill to generate humorous, meme-oriented LaTeX formulas that look profound while relying on trivial identities. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Using an online LaTeX renderer sends generated formula text to a separate service. <br>
Mitigation: Use a local renderer such as pdflatex, MathJax, or KaTeX when formula text should remain local. <br>
Risk: The skill runs a local Node.js script. <br>
Mitigation: Review the script and run it in an environment with Node.js available before relying on generated output. <br>


## Reference(s): <br>
- [Math Slop ClawHub page](https://clawhub.ai/0xmugen/skills/maths-rage-bate) <br>
- [artifact/README.md](artifact/README.md) <br>
- [artifact/SKILL.md](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [LaTeX text, usually shown as terminal output or Markdown inline code] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The CLI supports generating one formula by default or multiple formulas with --count.] <br>

## Skill Version(s): <br>
0.3.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
