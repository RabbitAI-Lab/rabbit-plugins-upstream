## Description: <br>
Smart image loader that handles both URLs and local files, automatically downloads URLs to temporary locations, and displays images using the read tool. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tingwei1123](https://clawhub.ai/user/tingwei1123) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent users use this skill to display images supplied as web URLs or local workspace file paths. It helps the agent download remote images to a temporary location, verify local image files, and return a path suitable for image display. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can fetch arbitrary image URLs and write downloaded files to temporary storage. <br>
Mitigation: Use trusted image URLs, avoid sensitive or unusual URLs, and review downloaded files before relying on them. <br>
Risk: The skill documentation recommends shell-based cleanup for file paths, which can be unsafe with user-controlled paths. <br>
Mitigation: Use safe file-deletion APIs or carefully quoted argument passing, and delete only verified temporary files. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [Plain text status output with file paths and cleanup guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce temporary local image files for downloaded URLs.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
