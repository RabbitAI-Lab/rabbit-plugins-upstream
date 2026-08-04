## Description: <br>
Depth Of Field Control helps agents give photography guidance for choosing aperture, focal length, focus distance, and hyperfocal settings to control background blur or keep a scene sharp. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bianchunhui](https://clawhub.ai/user/bianchunhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Photographers and photography assistants use this skill to decide how to adjust depth of field for portraits, products, landscapes, macro scenes, and phone photography. It helps an agent distinguish depth-of-field questions from exposure calculation, autofocus, motion, or post-processing blur issues. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may be invoked for exposure calculation, autofocus failures, motion blur, or post-processing blur requests that are outside its intended boundary. <br>
Mitigation: Route those requests to the appropriate exposure, focus, shutter-speed, or editing guidance before applying depth-of-field advice. <br>
Risk: Optical depth-of-field advice can be incomplete for phones and computational photography workflows. <br>
Mitigation: Explain the phone lens limitation and suggest portrait mode or moving closer to the subject when optical blur alone is insufficient. <br>
Risk: Incorrect camera-setting suggestions can produce misleading or unusable photos. <br>
Mitigation: Present aperture, focal length, and distance changes as practical guidance for user review rather than direct device control. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/bianchunhui/skills/depth-of-field-control) <br>
- [Server-resolved GitHub provenance](https://github.com/bianchunhui/nyip-photography-skills/tree/main/depth-of-field-control) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown or concise text guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [No file access, photo editing, or camera hardware control is expected.] <br>

## Skill Version(s): <br>
0.1.0 (source: server evidence release version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
