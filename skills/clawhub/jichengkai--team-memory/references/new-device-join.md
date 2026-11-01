# 新设备接入指南

适用：Amoo、OpenClaw和能执行Python脚本的其他客户端。程序3.0.1，记忆格式3.0，同步协议3.0。

## 1. 安装与准备

1. 解压 `team-memory-v3.0.1.zip`，将其中 `team-memory/` 安装到客户端的skill目录，启用该skill。只替换程序目录；保留旧版完整备份及独立记忆目录。
2. 确认 Python 3.10+ 可用，运行 `python3 <skill目录>/scripts/team-memory.py --version`，应显示3.0.1。Windows按环境用 `python` 替代 `python3`。
3. 为本设备配置Notion连接：允许读取、插入和更新正式云库页面及子页面，允许文件上传。将该集成添加到云库的Connections授权范围。
4. 在客户端安全的环境变量设置中配置 `TEAM_MEMORY_NOTION_TOKEN`，让智能体和后台子进程继承。不要在聊天中发送令牌，不把令牌写进skill、记忆JSON、标准包或共享脚本。两端可以用分别授权的连接。

## 2. 核对正式入口

从本云库首页复制正式页面链接，并核对：

- 云库入口：`ROOT_PAGE_ID`
- 库身份：`LIBRARY_ID`
- 状态必须为 `active`；页面标题为“团队记忆云库”。原“团队记忆云端备份”仅是迁移前档案。

以下命令中的尖括号内容需要替换。首次接入默认保存在 `~/.team-memory/libraries/<库身份>/`；指定其他空目录时，在 `library` 前添加 `--library-root <空目录>`。

```sh
python3 <skill目录>/scripts/team-memory.py library join --root-page <正式页面链接或UUID> --expected-library-id <库身份> --activate
python3 <skill目录>/scripts/team-memory.py library doctor
python3 <skill目录>/scripts/team-memory.py session status
```

join会下载最新完整快照与后续增量，逐文件核对哈希、原文、记录和修订关系，再重建索引。只有全部通过才切换到正式目录。`doctor.ok=true`、身份正确、`pending=0` 表示接入完成。

找不到页面、身份不符、包不完整或未知格式时，停止并处理错误；不能运行 `library init` 创建空库来绕过。已有非空目录用 `session prepare`，不能覆盖式join。

首次接入不复制另一设备的 `.runtime/`、机器身份、凭据、锁、活动库指针或日志。标准包也不会携带这些内容。

## 3. 启动后台与恢复运行

正常capture/checkpoint会按需启动独立worker。请让宿主应用允许后台进程，并在应用启动时执行一次：

```sh
python3 <skill目录>/scripts/team-memory.py worker run
```

有待提交时每60秒检查本端截止时间；空闲15分钟提交。没有待提交或待修复视图时退出，不调用模型。无需安排每分钟智能体心跳。移动端或电脑后台被暂停后，恢复脚本执行即可处理已到期批次；断网期间内容留在本端。

新一段团队沟通先 `session prepare --fresh`。普通追问用本端缓存；相关轮次结束执行checkpoint。明确“保存”“结束”“先这样”等结束意图时flush整批，不要等待15分钟。

## 4. 完成双端实机验收

1. 手机新增一条明确标为“接入验收”的测试事件，flush；记录云端版本和记录ID。
2. 电脑prepare，按ID读到事件；带当前expected_revision修订并flush。
3. 手机prepare，确认正文与新修订一致。
4. 新增测试内容并checkpoint，保持后台运行，15分钟后再加最多60秒检查周期，核对pending归零及已提交版本增加。
5. 临时断网保存另一条测试内容；确认只显示本端保存。恢复网络后由worker补传，再在另一端prepare核对。临时失败遵守Retry-After及退避时间。
6. 两端都确认后可明确删除测试记录（保留墓碑历史），再flush。

本次云库迁移回读验收与这组实机验收分别记录。安装前不能把实机验收写成已通过。

## 5. 日常状态

`session status`只返回版本、身份、待提交数量、冲突数量和异常。`queued`表示等待合并，`retry_pending`表示暂时失败等待补传，`paused`需要处理授权、权限或完整性问题；处理后 `session flush --retry`。`view_error`表示正式记忆已提交而派生页面暂时滞后，不代表原文丢失。

更新程序时直接替换skill目录，记忆留在独立目录。同格式更新不迁移数据。不要手工编辑Notion系统页或记忆包，通过智能体改动正式记录。
