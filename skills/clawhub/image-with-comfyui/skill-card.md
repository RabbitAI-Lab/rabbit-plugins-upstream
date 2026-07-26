## Description: <br>
Call a local ComfyUI instance for text-to-image (T2I), image-to-image/edit (I2I), and image-to-video (I2V) generation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sunshinejnjn](https://clawhub.ai/user/sunshinejnjn) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to generate images from text, edit supplied images, or create short videos from an image and prompt through an existing ComfyUI server. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The default configuration can send prompts and user images to a non-local ComfyUI server. <br>
Mitigation: Review config.json before installation and set COMFYUI_URL to a ComfyUI server you control, preferably localhost. <br>
Risk: Sensitive images or generated outputs may be stored in the configured media directory. <br>
Mitigation: Do not use sensitive images unless that endpoint and output location are acceptable for the use case. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/sunshinejnjn/skills/image-with-comfyui) <br>
- [README.md](README.md) <br>
- [ComfyUI Impact Pack](https://github.com/ltdrdata/ComfyUI-Impact-Pack) <br>
- [ComfyUI WAS Nodes](https://github.com/WASasquatch/ComfyUI-WAS-Nodes.git) <br>
- [ComfyUI Manager](https://github.com/comfyanonymous/ComfyUI-Manager.git) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Text, Shell commands, Guidance] <br>
**Output Format:** [Generated image or video files with brief text status and Markdown command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are saved under the configured media directory; image-edit and image-to-video modes send source images and prompts to the configured ComfyUI endpoint.] <br>

## Skill Version(s): <br>
1.5.0 (source: server release and openclaw metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
