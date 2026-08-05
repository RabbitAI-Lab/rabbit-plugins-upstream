## Description: <br>
Helps agents advise photographers on selecting shutter speeds to freeze motion, show motion blur, or use panning, while distinguishing those choices from depth-of-field and exposure calculation tasks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bianchunhui](https://clawhub.ai/user/bianchunhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and photography assistants use this skill when a photographer asks how to choose shutter speed for moving subjects, motion blur, freezing action, or panning technique. It provides starting shutter-speed ranges and decision factors based on subject speed, direction, distance, focal length, and creative intent. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill's shutter-speed recommendations can be too broad for a specific camera, lens, light level, stabilization system, or subject. <br>
Mitigation: Treat suggested speeds as starting points and adjust after checking exposure, sharpness, motion rendering, and camera shake in test frames. <br>
Risk: The skill is scoped to motion rendering and may be misapplied to depth-of-field, exposure calculation, static scenes, or general blur diagnosis. <br>
Mitigation: Use it only for shutter speed and motion rendering questions; route depth-of-field, exposure balancing, static scene, and whole-frame blur diagnosis to the appropriate workflow. <br>


## Reference(s): <br>
- [Server-resolved GitHub provenance](https://github.com/bianchunhui/nyip-photography-skills/tree/main/shutter-speed-motion) <br>
- [ClawHub skill page](https://clawhub.ai/bianchunhui/skills/shutter-speed-motion) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Text, Markdown] <br>
**Output Format:** [Markdown or plain text photography recommendations with shutter-speed ranges and panning steps] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Suggested shutter speeds are starting points and may need adjustment for camera, lens, light, stabilization, and subject behavior.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
