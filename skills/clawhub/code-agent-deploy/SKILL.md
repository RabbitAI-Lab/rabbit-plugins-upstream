---
name: code-agent-deploy
description: Deploys a local project and returns the address it can be opened at. Identifies the project, makes it ready to deploy, packs the source and hands it to the deployment platform to build and run (no Docker needed on this computer), repairs and retries from what the server reports, and afterwards shows status and logs and rolls back. For anything reached through a URL - websites, web applications, backend API services. The user only needs a deploy key and never touches a server.
---

# WEB DEPLOY: the deployment skill

## Goal

When the user says "deploy this project", take it from the local project to an address that opens, without making the user deal with Docker, servers or networking. The user only has to:

1. Run `appcli auth set-key` once in a terminal, the first time, and paste their own deploy key. They create it on the platform console's Deploy keys page (`/keys`); on a platform that is not open for registration an administrator issues it.
2. Confirm once the diff that makes the project ready to deploy.
3. On the first deployment, confirm which local file the runtime parameters are read from (when there are any).
4. On the first deployment, decide whether to migrate local data (asked only when local data is found; the default is no).

Commands, manifest fields, output and error codes are defined in the [appcli reference](references/appcli-reference.md).

**Language.** This skill is written in English; talk to the user in the language they use. The platform console is in Chinese, so its pages are named here by their path (`/keys`, `/plans`): name the page in the user's language and give the path. The questions and the report formats below are given in English; put them into the user's language as well.

## Rules that are never broken

1. Every deployment goes through the deployment platform, by running appcli. No SSH, no SCP, no direct connection to a server, no remote Docker.
2. Never read, print or ask for the deploy key. When it is missing, ask the user to run `! appcli auth set-key` in their own terminal. appcli is downloaded from the platform and carries that platform's address, so the command needs no `--platform`; add `--platform <platform address>` only when `platformUrl` in `appcli auth status` is null, or when the user explicitly wants another platform. A user who has no key yet opens the platform address (`platformUrl`), signs in and creates one on the Deploy keys page (`/keys`); on a platform that is not open for registration they ask the administrator.
3. Never put .env files, keys, tokens, database passwords, local databases or uploaded files into the image.
4. An upload that succeeded, or a task that is queued or running, is not a successful deployment. Wait for succeeded or failed.
5. Redact before showing logs: Authorization, Cookie, password, token, secret, private keys, passwords inside connection strings, and strings that start with `dpk_`.
6. Errors of category auth, server or platform are never worked around by another route. Never suggest opening SSH or the Docker API.
7. Do not change business code outside the checklist in section 2 unless it is explained separately and the user agrees.
8. Do not start containers locally as a rehearsal. Locally only static checks are done; deploy to the server and repair from what the server reports.

## Workflow

### 0. Before anything else

~~~bash
appcli version --json        # is appcli installed, what the platform supports, is anything out of date
appcli auth status --json    # are the key and the platform address configured
appcli plan --json           # what the user's plan gives: projects, memory and CPU per project, database services, builds (run it once the key is configured)
~~~

The image is built on the deployment platform's server. The developer's computer does not need Docker; do not ask the user to install or start it.

- appcli is not installed: tell the user it has to be installed from their platform (`npm install -g <platform address>/downloads/appcli`), and stop.
- Something is out of date (`updates` in `appcli version --json`): update first, then go on. Update each thing at most once in a conversation.
  - `updates.appcli.outdated` is true: tell the user in one sentence that the deploy tool has a new version and is being updated, run `updates.appcli.command`, then run `appcli version --json` again.
  - `updates.skill.outdated` is true: run `updates.skill.command`, then read the SKILL.md in the directory it prints again and start over from this section with the new instructions.
  - A failed update does not block the deployment: tell the user why it failed and go on with what is installed. When the output has no `updates`, or one of the two is absent, that check is not available; skip it.
- No key configured (`DEPLOY_KEY_MISSING`): ask the user to run `! appcli auth set-key` and continue when they have. Do not add `--platform`: appcli already carries its platform's address (`platformUrl` in `auth status`). Only when `platformUrl` is null is an address needed; use the one the user gives, as `! appcli auth set-key --platform <platform address>`. Never guess it.
- The platform cannot be reached (`PLATFORM_UNREACHABLE`): ask the user to check the platform address and the network they are on, and stop.
- A feature missing from the platform's capabilities: do not run the steps that need it, and say so in the result.
- The plan (`limits` in `appcli plan --json`; null means no limit) decides what the following steps can do. Look at it before choosing an approach:
  - `database` is `none`: the platform gives this user no MySQL / PostgreSQL database service, only SQLite can be used. `shared`: a shared instance can be used, a dedicated one (`mode: dedicated`) cannot. `dedicated`: both.
  - `memoryMb`, `cpus`: the ceiling for each project. Asking for more in the manifest is not an error: the platform runs the project at the ceiling and writes a `[plan]` line into the deployment's events.
  - `sleepAfterDays`: a project nobody has visited for this many days in a row is put to sleep (section 7).
  - `notices`: what is about to get in the way, each as a sentence that says what to do: the plan runs out within a week, its projects are all in use (no new project can be created), the builds of the day are nearly or fully used, projects are asleep because the plan has no room. Tell the user the ones that concern what they asked for **before** starting, so they are not met as a failure halfway. `plansUrl` is the page where the plan is changed.
  - When the command is not available (an older platform), skip it and assume no limits.

### 1. Identify the project

Read package.json / pom.xml / build.gradle / requirements.txt / pyproject.toml, the lock files, the framework configuration (next.config.*, vite.config.*, application.properties/yml, settings.py and so on), any existing Dockerfile / compose file / deploy.manifest.json, the **names** of the variables in .env* files (never output their values), and .gitignore.

Establish:

- The framework, how the application starts, and the port it really listens on.
- Whether it uses a database, which kind, and where the file is (where the SQLite file is; the major version of MySQL / PostgreSQL). MySQL / PostgreSQL are provided by the platform as a database service (a database of its own in a shared instance by default, a dedicated instance as an option); see [stack conventions](references/stacks.md). When the project needs a database service the user's plan does not include (section 0), tell the user before changing anything: either upgrade on the console's Plans page (`/plans`), or the user decides to move the project to SQLite. Changing the database is a business change; do not decide it yourself.
- Where attachments, uploads and generated files are written.
- The environment variables needed at run time, and which of them are build-time variables (such as `NEXT_PUBLIC_*`).
- Hard-coded localhost addresses and absolute local paths.
- Native dependencies (better-sqlite3, sharp, prisma and so on) and whether the build downloads anything.
- Where the local SQLite file and the attachment directories actually are (needed for the question in section 4.5).

When a manifest with an applicationId already exists, run `appcli status --json` first to learn the project's state, and skip the changes that are already made.

### 2. Make the project ready to deploy

Produce the changes in the table below, **show the whole diff once, and ask the user to confirm once**. A complete version that has passed acceptance on the platform is the [example project](references/example-nextjs-sqlite/) (Next.js + SQLite); follow it where it applies. For Java, Python and MySQL / PostgreSQL follow the [stack conventions](references/stacks.md). After the changes, local `npm run dev` must behave as before: every environment variable that is introduced defaults to the value the project used locally.

| Change | Requirement |
|---|---|
| Dockerfile | Multi-stage. For the base image prefer the platform's own `node-base` (written as the name alone); another public image may be used (with an explicit version), and anything needed may be installed or upgraded on top of either, see [base images](references/base-images.md). The runtime stage has `USER 10001` and copies only what is needed to run. For every variable in buildEnv the build stage has `ARG X` and `ENV X=$X`. With a migration tool, the start command runs the migration first (for example `prisma migrate deploy`) |
| .dockerignore | Excludes .env*, .appcli, node_modules, .next, .git, local databases (with their -wal / -shm files), upload directories and backups |
| .gitignore | Add `.appcli/` |
| .npmrc | Points at Alibaba's npmmirror, with binary mirrors for the dependencies that need them (see "npm registry" in base images); the Dockerfile copies it before `npm ci` |
| deploy.manifest.json | As in section 2 of the [appcli reference](references/appcli-reference.md); applicationId left empty; checked with `appcli validate --json` |
| Health check endpoint | `/api/health` by default, answering 200 with a small JSON body. It may do a read-only database check. It writes nothing and has no business logic. **It must be exempt from middleware such as login guards and i18n redirects** (in Next.js, exclude the path in the middleware's matcher) |
| Listening | Listen on `0.0.0.0`, on the port read from `PORT` |
| Next.js | `output: 'standalone'`; the standalone output also needs `public` and `.next/static` copied |
| Data paths | The database is read from `DATABASE_URL` (Java reads `JDBC_DATABASE_URL`, `DB_USER`, `DB_PASSWORD`), attachments from `UPLOAD_DIR`, generated files from `GENERATED_DIR` |
| Absolute addresses | Server-side code reads `PUBLIC_URL` (no trailing slash). Client-side code reads a `NEXT_PUBLIC_*` variable declared in the manifest's buildEnv as `from: "publicUrl"` |
| Cookies | An application with sign-in uses a cookie name that is unique to the project. The address is normally HTTPS; set the cookie's `Secure` attribute from the protocol of **the request** (the `X-Forwarded-Proto` header, for example Express `trust proxy`), or leave it unset when the framework cannot do that. Never hard-code it to true |

Notes:

- The root filesystem is read-only: the application can write only to the declared storage directories and to /tmp. When it writes anywhere else (for example `data/` or `public/uploads/` under the project directory), change it to read the matching environment variable and declare the directory in the manifest's storage.
- A Next.js application that uses image optimisation or ISR declares `/app/.next/cache` as ephemeral storage.
- Private attachments must not live in a public static directory; they are downloaded through an endpoint that checks who is asking.
- The project's own runtime version constraint comes first: choose `node-base` or a public image of the right version to suit it. Before using apt, switch to the Alibaba Cloud mirror (see base images).
- With native modules such as better-sqlite3, configure the binary mirror in `.npmrc` and prefer a version that has prebuilt binaries; when there is none, install python3, make and g++ in the build stage and compile from source. A new project can also consider Node's built-in `node:sqlite`, which needs no native build.
- `next/font/google` makes the build fetch from Google, which usually cannot be reached from mainland China: change to `next/font/local` and put the font files into the project. This is outside the checklist, so explain it separately and get the user's agreement.
- Build-time variables such as `NEXT_PUBLIC_*` go only into buildEnv, never into env. buildEnv never contains a secret.
- Everything the build downloads goes through Alibaba's npmmirror (npm packages and binaries); how to check is in base images. Do not switch to registry.npmjs.org or another registry abroad.

### 3. Static checks

Check before deploying and fix what is found (directly when it is within the checklist, otherwise explain it):

- Does the build context contain .env files, private keys, local databases or uploaded files?
- Does the Dockerfile COPY credentials or .env, or pass a secret in through `ARG`?
- Is a secret declared as `NEXT_PUBLIC_*` or placed in buildEnv?
- Is `.appcli/` in both .gitignore and .dockerignore?
- Does the manifest pass `appcli validate --json`?

### 4. Runtime parameters

On the first deployment, when the manifest declares env:

1. Classify each parameter as in "Two kinds of parameter whose value differs between local and live" in [personal project configuration](references/personal-configuration.md), and list its name, whether it is required, whether it is sensitive, and where its live value comes from (never its value):
   - A signing secret the application uses for itself (SESSION_SECRET, JWT_SECRET, NEXTAUTH_SECRET and the like): written as `generate` in the manifest by default, so the platform creates a new value.
   - A key that decrypts data already stored: when the user chooses to migrate local data it keeps the local value (`source`), otherwise `generate`.
   - Credentials of a third-party service: ask the user "Are these credentials for development and testing? Once the application is live, other people using it will spend this account's quota or cost money." To keep them use `source`; to use different ones use `manual` and ask the user to run `! appcli config set <NAME>` themselves.
   - Ordinary configuration: `source`.
2. Ask the user to confirm the local source file (for example `.env.local`). Only the declared parameters are submitted, never the whole file; registry credentials, deploy keys, private keys and variables that have nothing to do with this project are left out.
3. A value that is a localhost address or a path on this computer is pointed out; ask what the live value should be, do not guess.
4. When a deployment returns `CONFIG_MISSING_REQUIRED`: for the names in `details.manual` ask the user to run `! appcli config set <NAME>`; the names in `details.notInSource` are declared with a source file that does not contain them, so settle with the user where their value comes from. Deploy again when that is done.
5. Later deployments go by the platform's values; appcli only fills in what has been added and is missing (including creating a value for a newly added generate parameter).

The detailed rules are in [personal project configuration](references/personal-configuration.md).

### 4.5 Migrating local data (first deployment only, optional)

Only when the project has never been deployed successfully (the manifest has no applicationId, or `everSucceeded` in `appcli status --json` is false) and a local SQLite file or attachment directory is found, or the project uses a local MySQL / PostgreSQL. MySQL / PostgreSQL data is migrated through a SQL dump the user exports (how is in [stack conventions](references/stacks.md)); the AI never connects to the user's database itself:

1. List what would be migrated: the database file's path and size; for each attachment or generated-files directory its path, number of files and total size.
2. Point out that it may contain test data or personal information, and ask whether to migrate it. **The default is not to migrate**: when the user refuses, does not clearly agree, or does not answer, nothing is migrated.
3. When the user agrees: fill in `database.localPath` in the manifest (the local database file, as a path relative to the project) and `localPath` of the storage entries (the attachment and generated-files directories), and deploy with `--import-data`. appcli makes a consistent snapshot; do not copy .db files by hand.
4. appcli remembers the agreement (tied to the project ID): automatic retries before the first success bring the data along without asking the user again. When the project ID changes, the agreement is void.
5. A project that has been deployed successfully cannot import any more (`DATA_IMPORT_NOT_ALLOWED`); tell the user the live data will not be overwritten.

### 4.6 Backup before deploying (a project setting)

When the project has a database (`database.type` in the manifest is sqlite, mysql or postgres) and the manifest has no `backupBeforeDeploy` yet, ask the user once before the first deployment: "From now on, before every deployment and rollback, should the database be backed up on the server first? (Recommended: the five most recent are kept, and they can be restored if something goes wrong.)"

- The user agrees, does not clearly refuse, or does not answer: write `"backupBeforeDeploy": true`.
- The user clearly does not want it: write `"backupBeforeDeploy": false`, and tell them there will then be no pre-deployment backup to restore from if something goes wrong.
- From then on the setting is followed without asking again; when the user wants it changed, change the manifest.
- For a one-time exception use `appcli deploy --backup` or `--no-backup` and leave the manifest alone.
- A project without a database is not asked, and the field is not written.

### 5. Deploy

~~~bash
appcli deploy --wait --wait-timeout 540 --json                 # the default
appcli deploy --import-data --wait --wait-timeout 540 --json   # when the user agreed to migrate local data
appcli deploy --no-backup --wait --wait-timeout 540 --json     # when the user asked for no pre-deployment backup this once (--backup is the opposite)
~~~

appcli does it all: creates the project (the first time) → fills in parameters → packs the source → uploads it in parts → creates the task → waits for the platform to build the image and the server to run it. After the first deployment check that applicationId has been written into the manifest.

- `--wait-timeout 540` makes one call return within a tool call's time limit. When it returns `WAIT_TIMEOUT` the task is still running: keep waiting with `appcli deployment <deploymentId> --wait --wait-timeout 540 --json`. Do not deploy again.
- The deploymentId is written to `.appcli/state.json` as soon as the task is created; when a call is interrupted, take it from there.
- When the user asks to stop, `appcli cancel <deploymentId>` cancels a task that is waiting to be built, being built, or waiting for the server. Once the server is running it, it cannot be cancelled; wait for it to end.
- Output with `"pending": true` is a task still on its way (the command did not wait): neither a success nor an error. Wait for it with the command in `next`.

### 6. Results and automatic repair

Success: report the address (the format is in section 9).

Failure: act on `error.category`:

| category | What to do |
|---|---|
| build, app | A failed build (on the platform's server): read `error.details.buildLogTail` (the last 200 lines of the build log; `appcli deployment <id> --wait` prints all of the task's events, the whole build log among them, to standard error). A failed run: read `result.logTail`, `container` and `health`. Change the project and deploy again |
| transient | By error code. `DUPLICATE_DEPLOYMENT`: wait for the task in progress first (its ID is in `error.details.deploymentId`). `WAIT_TIMEOUT`: keep waiting with `appcli deployment`. `PREVIOUS_TASK_UNRESOLVED`: tell the user a deployment's result is not known yet, and try again later. `PORT_IN_USE`, `BUILD_INTERRUPTED` and the upload errors: deploy once more, unchanged (when `PORT_IN_USE` fails again, report the error code and suggest contacting the administrator; the address will not change) |
| auth, local_env, user_input | Stop and say what the user needs to do |
| server, platform | Do not change the project and do not retry over and over. Report the error code and message and suggest contacting the administrator. `AGENT_LOST` (status lost) means the result is not known for now: tell the user, and ask later with `appcli deployment <id>`; it may be corrected to the real result. `RESULT_UNKNOWN` means there was still no result after 24 hours; see with `appcli status` which version the project is really running |

user_input errors about the project itself: on `APPLICATION_NOT_FOUND` or `APPLICATION_DEACTIVATED`, ask the user whether to empty the applicationId in the manifest and deploy as a new project. A new project gets a new address and none of the old data; an earlier agreement to migrate data no longer holds, so ask again if there is local data. A deactivated project can also be brought back by the administrator within 30 days, with its address unchanged.

Errors about the plan (none of them is a problem of the project: do not change the project to get around them and do not retry over and over). Each one's `message` says which limit it is and what can be done, `error.details.reason` names the limit for a program (`project_quota`, `projects`, `database`, `database_dedicated`, `builds`, `versions_kept`), and `error.details.plansUrl` is the page where the plan is changed. Pass the message on in the user's language, with that address:

| Error code | What to do |
|---|---|
| `APPLICATION_ASLEEP` | The project is asleep. Run `appcli wake --wait --json`, and when it succeeds retry the original command (`appcli deploy` wakes the project itself and does not meet this error) |
| `PLAN_LIMIT_EXCEEDED` | The plan has no room: too many projects, or a database service the plan does not include. Pass the `message` on to the user and ask them to upgrade on the console's Plans page (`/plans`), or to deactivate projects they no longer need |
| `BUILD_QUOTA_EXCEEDED` | The builds of the last 24 hours are used up. Tell the user they can deploy again after `details.retryAt`, or upgrade the plan; do not retry before then |
| `TERMS_NOT_ACCEPTED` | The platform's user agreement was updated. Run `appcli console` and ask the user to open the link and agree; retry after they have |
| `DATA_QUOTA_EXCEEDED` | The project stores more (files plus database, `details.usedMb`) than the plan gives one project (`details.limitMb`). Deploying again does not help: tell the user to delete data the app no longer needs, or to upgrade the plan |
| `PROJECT_QUOTA_EXCEEDED` | The number of projects is at its limit and no new project can be created. As above: upgrade, or deactivate another project |

`notices` in the output of a deployment (the same sentence is a `[plan]` line among its events) means this deployment runs at the plan's memory / CPU ceiling, below what the manifest asks for; it is there on a failed deployment as well as on a successful one. If the application then fails to start and it looks like too little memory (container exit code 137, OOM in the logs, `JavaScript heap out of memory`), do not try to fix it by raising memory in the manifest (it has no effect): tell the user the plan's memory ceiling per project and let them decide between upgrading the plan and making the application use less.

Rules for automatic repair:

- At most 3 automatic redeployments for one request to deploy. When it still fails, stop, summarise each error and each change made, and let the user decide.
- Repairs stay within the checklist. When business code or data structures would have to change, explain first and get agreement.
- Before each repair say what the judgement rests on (quote the log lines).
- `restoredPrevious: true` means the address is still serving the previous version. Tell the user so; there is no need to retry in a hurry.
- When the first deployment fails, the address does not work yet.

Common failures and where to look:

| What is seen | Usual cause | Repair |
|---|---|---|
| BUILD_FAILED, npm download fails or times out | npmmirror is not in use (for example `.npmrc` is not copied into the build stage, or `.dockerignore` excludes it) | Check that `.npmrc` exists, is not excluded and is copied before `npm ci`, and that the addresses in yarn.lock are replaced. The platform's server itself can reach npmmirror |
| REGISTRY_UNREACHABLE | The base image cannot be pulled for the build | Check that the image name and version tag exist. Registries other than Docker Hub may be unreachable: change to an equivalent image on Docker Hub, or to `node-base`. When `node-base` cannot be pulled either, it is the server's problem: tell the user to contact the administrator |
| SOURCE_INVALID | The source contains something that is not allowed (a link pointing outside the project and the like), is over 500 MB, or the Dockerfile is not in the package | Adjust `.dockerignore` or the dockerfile path in the manifest as the message says; exclude large files with `.dockerignore` |
| BUILD_TIMEOUT | The build took more than 30 minutes | Look for a large download or a network request that hangs during the build; reduce the build steps |
| BUILD_FAILED, an install script times out reaching github.com | A package downloads a binary and has no mirror configured | Configure the npmmirror binary mirror for that package in `.npmrc` or as ENV in the build stage |
| BUILD_FAILED, compiling a native module or downloading its prebuilt binary times out | The build stage lacks the build tools, or is trying to download the prebuilt binary from GitHub | Use a version that has prebuilt binaries, or install the build tools in the build stage and compile from source (see base images) |
| CONTAINER_START_FAILED, Cannot find module | The standalone output lacks files, or a native module was not copied | Correct the copy steps in the Dockerfile |
| CONTAINER_START_FAILED, EACCES / EROFS | Something is written to a directory that is not declared, or the directory's permissions are wrong | Move the write to declared storage or /tmp and add the storage declaration |
| HEALTHCHECK_FAILED, connection refused | Listening on 127.0.0.1, or on another port | Listen on 0.0.0.0, read PORT, check containerPort |
| HEALTHCHECK_FAILED, 404 | The health path does not exist | Check healthcheckPath against the routes |
| HEALTHCHECK_FAILED, lastStatus is 3xx | The health endpoint is caught by a login guard or an i18n redirect (see lastLocation) | Exclude the health path in the middleware |
| HEALTHCHECK_FAILED, timed out | Slow start, or a long migration | Raise healthTimeoutSeconds (at most 600) and read the logs |
| A missing environment variable at start / CONFIG_MISSING_REQUIRED | A required parameter is not declared or was not submitted | Add the env declaration, confirm its source with the user as in section 4, and submit |
| A client-side variable is empty (`NEXT_PUBLIC_*` undefined) | The build-time variable was not passed through buildEnv (or `buildEnvMissing` in the deploy output names it: its source file does not have it), or the Dockerfile does not declare the ARG | Add buildEnv and the Dockerfile's ARG / ENV |
| The page opens but assets or links are 404, or go to localhost | A hard-coded absolute address | Use PUBLIC_URL |
| PLATFORM_MISMATCH | The image that was built is not linux/amd64 (a `FROM --platform=...`, or a base image that exists only for another architecture) | Remove the platform override, or choose a base image that has a linux/amd64 build |
| Deployed, but signed out again right after signing in | The cookie is marked Secure while the address is plain HTTP (or the auth library forces Secure in production), so the browser does not keep it | Set Secure from the request's `X-Forwarded-Proto`, or not at all; give NextAuth and similar libraries PUBLIC_URL as their URL |
| Works locally, one feature fails live | A browser API that exists only in a secure context (crypto.subtle, the clipboard, the camera, Service Workers) on an address served over plain HTTP | Tell the user about the limit. Replace it with something that does not need a secure context where that is possible; otherwise say the feature is not available on that address |

Never repair by turning the health check off, running as root, or turning the read-only filesystem off.

### 7. Everyday operations

~~~bash
appcli status --json
appcli logs --tail 200 --json
appcli logs --follow
appcli deployments --json
appcli config get --json
appcli config set NAME          # the value is typed in (the user runs this in their own terminal)
appcli config regenerate NAME   # a new signing secret; after apply, signed-in users are signed out
appcli config apply --wait --json
appcli deployment <id> --wait --json
appcli cancel <id>
appcli backups --json
appcli console                  # a one-time sign-in link that opens the console
appcli wake --wait --json       # wakes a sleeping project
appcli plan --json              # the plan, its limits and what is used
~~~

Asleep: when `status` in `appcli status` is `sleeping`, the platform has stopped the project. Its data, its address and its earlier versions are all kept, and it still takes one of the plan's projects. `sleepReason` says why:

- `idle`: nobody visited it for days in a row (the plan's `sleepAfterDays`). The platform wakes it when someone opens the address; that first visit takes ten seconds or so. `appcli wake --wait --json` wakes it too. When the user asks why the site "does not open" or "says it is starting", look for this state first.
- `plan`: the plan has no room for it (the plan ran out and the user is back on the free plan, there are too many projects, or it uses a database service the plan does not include). `appcli wake` then returns `PLAN_LIMIT_EXCEEDED` and the address shows a "paused" page. Once the user renews or upgrades, the platform wakes it by itself; nothing needs to be deployed again.

`sleepNote` in `appcli status` says, for the project in hand, which of these it is and what brings it back; pass it on.

While a project is asleep its status, logs and deployments can be read and runtime parameters can be saved. Restarting, rolling back, applying parameters and restoring data need it awake first. When waking fails (the application does not come up) the project stays asleep: report the error code and the logs and suggest contacting the administrator.

Data is restored only when the user explicitly asks, and after the user has confirmed which backup (which point in time) to restore:

~~~bash
appcli restore --backup <backupId> --confirm <applicationId> --wait --json
~~~

Tell the user: a restore replaces only what the backup contains (a pre-deployment backup holds the database only and does not touch attachments; there are no scheduled backups; a project with pre-deployment backups turned off has only "pre-restore" backups). The application stops briefly during the restore. The data that is replaced is kept as a "pre-restore" backup for 14 days and can be restored with the same command. A restore that fails is undone automatically. A project that has never been deployed successfully cannot be restored.

A project is deleted only when the user explicitly asks, and after the user has confirmed the project ID:

~~~bash
appcli delete --confirm <applicationId> --wait --json
~~~

Tell the user: this deactivates the project, it does not delete it at once. The container stops and the address closes; the data, the port and the address are kept for 30 days, during which the platform's administrator can bring it back (same address). Only after 30 days can the administrator delete it for good. A deactivated project cannot be deployed again, unless the applicationId in the manifest is emptied and it is deployed as a new project.

### 8. Rolling back

Only when the user explicitly asks:

~~~bash
appcli deployments --json
appcli rollback --to <deploymentId> --wait --json
~~~

Only versions that `appcli deployments` lists with `canRollback: true` can be gone back to: the plan keeps a number of earlier versions (`versionsKept` in `appcli plan`) and the images of older ones are cleaned up. A rollback to one of those returns `ROLLBACK_NOT_ALLOWED` with `details.reason` `versions_kept`; offer the user the versions that are still kept, or deploying that code again.

Report the version before and after. A rollback uses the target version's own settings (port, storage, resources) with the runtime parameters as they are saved now; before it, the server backs up the database as the project is set (backupBeforeDeploy). A rollback does not restore the database or the attachments: when the newer version made a migration that is not backward compatible, warn the user of the risk, and when needed combine it with a restore of the pre-deployment backup.

### 9. What to hand over

Success:

~~~text
Address: https://<the domain the platform assigned>/ (public access: on)
Project ID: todo-app-k3f9
Deployment ID: dep_...
Changes made: (list of files)
Persistent directories: database /app/data, attachments /app/uploads (bound)
Runtime parameters: 3 submitted, 1 generated by the platform (SESSION_SECRET), 1 typed in by the user (OPENAI_API_KEY), 0 missing
Local data: not migrated / migrated (1 database, 230 attachment files)
Note: the entry was verified from the server itself; whether visitors' networks can reach it was not verified
Plan: Free; running at the plan's ceiling (256m memory, 0.25 CPU; the manifest asks for 512m / 1); after 7 days without a visit it goes to sleep and wakes when opened again (ten seconds or so)
~~~

The "Plan" line says only what concerns this deployment: that it runs at the ceiling (the output has `notices`), that it will sleep when idle (`sleepAfterDays` is not null), and any of the plan's own `notices` the user should act on soon (it runs out in a few days, the builds are nearly used up). When none applies, leave the line out.

Failure:

~~~text
Project ID / deployment ID:
Stage it failed in, and the error code:
What is live: still the previous version / nothing running
Key log lines (redacted):
Repairs tried (attempt n):
What the user has to decide, or the administrator has to handle:
~~~

## What may be changed

May be changed (after the user confirms the diff): the files and code points in the checklist of section 2, and the local appcli configuration.

Not changed: any server configuration, firewalls, Nginx, other projects, database structure, business logic (unless agreed separately). Problems on the server side are reported with their error code and evidence.

## Data and storage

- SQLite by default. `database.path` in the manifest defaults to `/app/data/app.db`, and the platform injects `DATABASE_URL=file:<database.path>`. When the driver the project uses wants another URL format, adapt how the project reads it; the project's code decides.
- `UPLOAD_DIR` and `GENERATED_DIR` are injected only when the manifest declares storage named uploads and generated; their values are those entries' mountPath.
- The database, the attachments and the files generated for good are each declared persistent; caches are ephemeral.
- Local data is not uploaded with a deployment by default. Migrating it is the user's decision, and is possible only before the project's first successful deployment, with `--import-data` (section 4.5).
- Releases and rollbacks do not reset the database and do not overwrite attachments. Do not create test data in the user's live project.

## The entry

- The address is assigned by the platform, does not change after deployment, and is whatever appcli returns: `externalUrl`, a second-level domain the platform assigns (its form is the platform's, for example `https://<project ID>.<domain>/`). It is the application's only address. `publicUrl` is the `PUBLIC_URL` injected into the application, and is the same. HTTPS ends at the platform's gateway: the application listens on plain HTTP and configures no domain or certificate of its own; the request header `X-Forwarded-Proto` is the protocol the visitor really used. Do not guess the address and do not hard-code an example address.
- Public access is on by default (`externalAccess`). After the first successful deployment, hand over the address appcli returned and say that anyone can open it; when the application holds internal data or can be written to, remind the user to make sure sign-in protects it. Then ask whether to keep public access. To turn it off run `appcli access external off --json` (`appcli access external on --json` turns it on again). Say what follows before turning it off: the application cannot be reached until it is turned on again. When the user wants another prefix for the domain, run `appcli access name <prefix> --json` (3 to 63 lower-case letters, digits and hyphens; `SUBDOMAIN_UNAVAILABLE` when it is taken, ask the user for another), and tell the user the old address stops working afterwards and may be taken by someone else; PUBLIC_URL changes with the next deployment or apply.
- The application runs at the root path `/`; do not add a basePath.
- A successful deployment means the server itself reached the application through the entry. Whether visitors' networks can reach it is not verified by this skill; say so honestly in the report.
