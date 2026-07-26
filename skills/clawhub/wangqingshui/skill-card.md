## Description: <br>
This skill guides an agent to invoke a local Mengpo-style narrative engine for generating memory-themed monologues and share-card content without modifying the protected engine logic. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ninebirds01-crypto](https://clawhub.ai/user/ninebirds01-crypto) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and creators use this skill to generate or integrate Mengpo-style emotional memory monologues, share-card text, and invocation guidance while preserving the narrative engine's required call contract. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The optional self-test loads local project modules from the intended engine project. <br>
Mitigation: Review the copied selftest.js and run it only inside the trusted engine project where those local modules are expected. <br>
Risk: The wrapper is strongly coupled to the engine's compose argument order, key mappings, and relationship combinations, so engine drift can cause incorrect or empty output. <br>
Mitigation: Run the documented guardrail self-test before release or upgrade and keep invocation-layer changes separate from protected engine logic. <br>
Risk: Users may provide personal memory content for emotional storytelling. <br>
Mitigation: Keep generated memory content local unless the surrounding application clearly discloses and controls any sharing or storage behavior. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/ninebirds01-crypto/skills/wangqingshui) <br>
- [Publisher Profile](https://clawhub.ai/user/ninebirds01-crypto) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JavaScript and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include optional self-test guidance; the skill itself is a documentation-style wrapper and does not execute the narrative engine.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
