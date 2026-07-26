## Description: <br>
Apply Critical Fallibilism to make decisions by binary testing ideas for decisive flaws, managing complexity, embracing criticism, and avoiding overreach. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xertrov](https://clawhub.ai/user/xertrov) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users, developers, and agents use this skill to structure high-stakes decisions, complex debugging, disagreement resolution, and self-correction with binary evaluations and explicit error-correction paths. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill includes guidance that may suggest shell actions such as reverting state during error correction. <br>
Mitigation: Keep command approval enabled and review any proposed shell command before execution, especially destructive version-control operations. <br>
Risk: The skill encourages retaining corrected refutations or process lessons in memory. <br>
Mitigation: Allow memory updates only after review, and exclude sensitive or unwanted information from retained corrections. <br>
Risk: The skill is an opinionated decision framework that may be inappropriate when probabilistic analysis or domain-specific methods are required. <br>
Mitigation: Use it as a reasoning aid and cross-check high-impact conclusions against domain expertise and applicable operational requirements. <br>


## Reference(s): <br>
- [Critical Fallibilism Forum](https://discuss.criticalfallibilism.com/) <br>
- [Ember's Blog](https://ember.vecnet.ai) <br>
- [Theory of Constraints](https://en.wikipedia.org/wiki/Theory_of_constraints) <br>
- [Karl Popper's Falsifiability](https://en.wikipedia.org/wiki/Falsifiability) <br>
- [Rationality on ClawHub](https://clawhub.ai/xertrov/skills/rationality) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands] <br>
**Output Format:** [Markdown guidance with structured templates, checklists, and occasional user-approved command suggestions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only reasoning aid; outputs should remain reviewable by the user before acting on command, memory, or process changes.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
