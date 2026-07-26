## Description: <br>
Provides Foxtable mobile development documentation covering HTML, WeUI, WeChat integration, client APIs, JSON parsing, asynchronous programming, and Web data sources. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[golgys0621](https://clawhub.ai/user/golgys0621) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to answer questions and produce implementation guidance for Foxtable mobile and Web development. It is most relevant for Foxtable projects involving WeUI pages, WeChat integrations, HTTP clients, JSON/XML data handling, asynchronous operations, generated reports, and Web data sources. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Documentation examples may lead users to expose Foxtable HTTP services or use weak defaults when moving from examples to production. <br>
Mitigation: Prefer localhost binding during development; use HTTPS, authentication, authorization, least-privilege execution, and firewall rules before exposing services. <br>
Risk: Examples involving WeChat, user identity, reports, files, uploads, and location data may affect sensitive or personal data. <br>
Mitigation: Use secret placeholders or secret managers, avoid storing passwords in cookies, apply server-side sessions, validate uploads, and define privacy and retention controls. <br>
Risk: Legacy reference material may contain patterns that are not secure-by-default for generated production code. <br>
Mitigation: Treat generated implementation advice as reference guidance and require security review, parameterized data access, and current platform documentation checks before deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/golgys0621/skills/foxmobile-dev-doc) <br>
- [Skill definition and reference index](SKILL.md) <br>
- [关于文档构成](references/00_关于文档构成.md) <br>
- [关于移动开发](references/01_关于移动开发.md) <br>
- [关于功能演示](references/02_关于功能演示.md) <br>
- [关于网页设计](references/03_关于网页设计.md) <br>
- [HTML入门](references/04_HTML入门.md) <br>
- [WeUI框架](references/05_WeUI框架.md) <br>
- [扩展WeUI的功能](references/06_扩展WeUI的功能.md) <br>
- [客户端类](references/07_客户端类.md) <br>
- [JSON解析](references/08_JSON解析.md) <br>
- [微信接口](references/09_微信接口.md) <br>
- [更多接口](references/10_更多接口.md) <br>
- [生成并发送PDF文件](references/11_生成并发送PDF文件.md) <br>
- [生成并发送Word文件](references/12_生成并发送Word文件.md) <br>
- [用Excel报表生成网页](references/13_用Excel报表生成网页.md) <br>
- [类型参考](references/14_类型参考.md) <br>
- [异步编程](references/15_异步编程.md) <br>
- [Web数据源](references/16_Web数据源.md) <br>
- [WeChat Official Account documentation](https://developers.weixin.qq.com/doc/) <br>
- [WeCom API documentation](https://work.weixin.qq.com/api/doc/) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown answers with Foxtable code snippets, command examples, and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only skill; outputs should be reviewed before applying examples to production services.] <br>

## Skill Version(s): <br>
2.0.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
