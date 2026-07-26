## Description: <br>
Search and download GIFs from Tenor API with caching, bulk download, and format conversion. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[itspremkumar](https://clawhub.ai/user/itspremkumar) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, content creators, social bot builders, and agent developers use this skill to search Tenor and retrieve GIF or media URLs from a command-line workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: GIF search terms and API keys are sent to Tenor during normal use. <br>
Mitigation: Use the skill only when sharing those search terms with Tenor is acceptable, and prefer setting a caller-controlled TENOR_API_KEY. <br>
Risk: The documented raw GitHub install URL is mutable. <br>
Mitigation: Pin or review the downloaded script before deployment. <br>
Risk: The security evidence notes risky CI helper code outside normal GIF-search runtime. <br>
Mitigation: Do not run ci/verify_product.py on untrusted folders unless it is sandboxed. <br>
Risk: The current code mainly prints GIF and media URLs rather than fully downloading, caching, or converting files. <br>
Mitigation: Review runtime behavior against workflow needs before relying on download, cache, or conversion claims. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/itspremkumar/skills/gif-search) <br>
- [Tenor API endpoint](https://tenor.googleapis.com/v2) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, code, guidance] <br>
**Output Format:** [Command-line text output with GIF IDs, descriptions, and media URLs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires network access to Tenor; set TENOR_API_KEY to use a caller-controlled API key.] <br>

## Skill Version(s): <br>
2.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
