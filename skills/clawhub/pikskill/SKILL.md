---
name: pikpak
description: "Manage PikPak cloud storage via pikpakcli: browse, upload, download, delete, rename, share, offline download."
---
# intro
This is a skill for agent using pikpakcli to download with links and manage pikpak cloud drive with pikpakcli 

pikpakcli could be used to download youtube link ,magnet link,torrent file,direct link.

pikpakcli could ls files in pikpak cloud drive,remove files in clould drive,agent could manage and check quota for user with pikpakcli



# start up

## install
in workspace :

### Compiling from source code

To build the tool from the source code, ensure you have [Go](https://go.dev/doc/install) installed on your system.

Clone the project:

```bash
git clone https://github.com/52funny/pikpakcli
```

Build the project:

```bash
go build
```

Run the tool:

```
./pikpakcli

## config
config using pikpakcli setup --force
required user prompt ：username&passsword.
verify the config with pikpakcli ls .
  


# instruction:
you can use interactive console with 

```
pikpakcli shell
```

## 新建

### 新建文件夹

- 在 Movies 下新建文件夹 NewFolder

  ```bash
  pikpakcli new folder -p Movies NewFolder
  ```

### 新建 Sha 文件

- 在 Movies 下新建 Sha 文件

  ```bash
  pikpakcli new sha -p /Movies 'PikPak://美国队长.mkv|22809693754|75BFE33237A0C06C725587F87981C567E4E478C3'
  ```

### 新建磁力

- 新建磁力文件

  ```bash
  pikpakcli new url 'magnet:?xt=urn:btih:e9c98e3ed488611abc169a81d8a21487fd1d0732'
  ```

## 配额

- 获取 PikPak 云盘的空间

  ```bash
  pikpakcli quota -H
  ```

## 获取目录信息

- 获取根目录下面的所有文件信息

  ```bash
  pikpakcli ls -lH -p /
  ```

## 删除

- 按完整路径删除文件

  ```bash
  pikpakcli delete /Movies/Peppa_Pig.mp4
  ```

- 使用 `-p` 指定父目录后删除其中的文件或文件夹

  ```bash
  pikpakcli delete -p /Movies Peppa_Pig.mp4
  ```

- 在同一路径下同时删除多个文件或文件夹

  ```bash
  pikpakcli delete -p /Movies File1.mp4 File2.mp4
  ```



