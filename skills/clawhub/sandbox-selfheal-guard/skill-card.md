## Description: <br>
Anti-stuck and anti-snapshot-wipe guard for agentic sandboxes with a bundled self-heal runner, byte-verified GGUF manifest, native CPU rebuild, hard timeouts, binary fallback, prompt-cache integration, and light-swarm auto mode. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to make sandboxed agent runs recover from missing local binaries, missing model files, stalled inference calls, and snapshot-size related failures. It provides shell-based recovery behavior for llama.cpp and GGUF model workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The runner may install apt packages, create a local npx shim, alter PATH for its process, rebuild llama.cpp, and download large GGUF files into the user's home directory. <br>
Mitigation: Run the skill in a disposable sandbox or review the shell script before use; add explicit prompts before host changes when deploying it in shared or persistent environments. <br>
Risk: Model downloads are checked by byte size but do not provide strong cryptographic verification for downloaded model contents. <br>
Mitigation: Pin model sources and add hash verification for every downloaded GGUF before using the models in a trusted workflow. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/sandbox-selfheal-guard) <br>
- [Publisher profile](https://clawhub.ai/user/orionshaowswmw) <br>
- [Qwen2.5 0.5B Instruct GGUF](https://huggingface.co/second-state/Qwen2.5-0.5B-Instruct-GGUF) <br>
- [Qwen3 0.6B GGUF](https://huggingface.co/bartowski/Qwen_Qwen3-0.6B-GGUF) <br>
- [DeepSeek R1 Distill Qwen 1.5B GGUF](https://huggingface.co/bartowski/DeepSeek-R1-Distill-Qwen-1.5B-GGUF) <br>
- [Qwen2.5 Coder 0.5B Instruct GGUF](https://huggingface.co/bartowski/Qwen2.5-Coder-0.5B-Instruct-GGUF) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, code] <br>
**Output Format:** [Markdown guidance with bash code and configuration details] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May describe timeout, fallback, cache, model manifest, and local recovery behavior for sandboxed CPU inference workflows.] <br>

## Skill Version(s): <br>
2.0.1 (source: server release metadata; artifact frontmatter says 2.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
