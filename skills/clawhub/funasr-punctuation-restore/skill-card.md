## Description: <br>
Restores Chinese and English punctuation for pasted text, single .txt files, or mirrored batches of .txt files using the FunASR ct-punc model. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wangminrui2022](https://clawhub.ai/user/wangminrui2022) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to add punctuation to ASR transcripts, unpunctuated text, individual .txt files, or directory trees of text files while preserving source inputs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill creates or reuses a local Python environment and automatically installs or mutates packages, including large or unrelated audio packages. <br>
Mitigation: Run it in an isolated environment, review the scripts before first use, and approve dependency installation only for trusted inputs and workspaces. <br>
Risk: The skill downloads FunASR model assets and Python packages from network sources during execution. <br>
Mitigation: Use controlled network access, pre-cache trusted model and package artifacts when possible, and verify package indexes or mirrors before use. <br>
Risk: The skill reads and writes user-selected text files or directories and creates derived output files. <br>
Mitigation: Point it only at intended text paths, keep backups of important directories, and review generated _punctuated outputs before replacing source material. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/wangminrui2022/skills/funasr-punctuation-restore) <br>
- [Publisher profile](https://clawhub.ai/user/wangminrui2022) <br>
- [ModelScope FunASR ct-punc model](https://modelscope.cn/models/damo/punc_ct-transformer_cn-en-common-vocab471067-large) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and generated punctuation-restored text or .txt files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create sibling _punctuated files or mirrored directories and cache model files locally.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
