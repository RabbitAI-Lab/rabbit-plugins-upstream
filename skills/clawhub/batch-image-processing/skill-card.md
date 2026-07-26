## Description: <br>
Batch Image Processing helps agents guide image compression, format conversion, and directory reorganization workflows using Pillow, jpegoptim, shell commands, and reusable Python scripts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[liuyunss](https://clawhub.ai/user/liuyunss) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to plan and run batch image compression, image-to-JPEG conversion, resumable processing, and metadata-based directory cleanup. It is suited for local or controlled remote image-processing jobs where users can review paths, quality settings, thread counts, and generated scripts before execution. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review flags unsafe SSH automation guidance, including disabling host identity checks for remote execution. <br>
Mitigation: Use the skill only with hosts and keys you control, avoid root SSH where possible, and replace disabled host-key checking with known_hosts provisioning, host-key pinning, SSH certificates, or another verified host identity workflow. <br>
Risk: Batch compression and directory reorganization can overwrite, skip, move, or degrade large image collections if paths, quality settings, or dry-run results are wrong. <br>
Mitigation: Run dry-runs for reorganization, use separate output directories, keep backups of source data, and review quality, thread count, and source/destination paths before running generated commands or scripts. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/liuyunss/skills/batch-image-processing) <br>
- [artifact/SKILL.md](artifact/SKILL.md) <br>
- [artifact/scripts/compress_generic.py](artifact/scripts/compress_generic.py) <br>
- [artifact/templates/img_compress.py](artifact/templates/img_compress.py) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands] <br>
**Output Format:** [Markdown guidance with Python and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce reusable Pillow-based compression scripts, command examples, progress-reporting patterns, and directory organization guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
