---
name: github-actions-pipeline-generator
version: "1.0.0"
category: devops
tags:
  - github-actions
  - ci-cd
  - pipeline
  - automation
  - yaml
  - deployment
  - testing
  - release
  - workflow
model: claude-sonnet-4-20250514
trigger_keywords:
  - GitHub Actions
  - CI/CD pipeline
  - workflow
  - GitHub workflow
  - continuous integration
  - continuous deployment
  - build pipeline
  - release automation
  - YAML pipeline
  - CI pipeline
pricing: "$7.99 one-time"
---

# GitHub Actions Pipeline Generator

> **Generate production-ready CI/CD pipelines tailored to your stack.** Detects language/framework, creates lint→test→build→deploy workflows with caching, matrix builds, security scanning, and release automation. Outputs valid YAML with reusable workflows.

## Why This Skill Exists

Writing GitHub Actions from scratch is error-prone: YAML syntax issues, missing caching, insecure secrets handling, and no deployment rollback. This skill generates battle-tested pipeline templates that follow GitHub's best practices and your team's stack.

## When to Activate

Activate when the user:
- Creates a new project and needs CI/CD
- Asks for a GitHub Actions workflow, pipeline, or CI/CD setup
- Mentions `.github/workflows`, GitHub Actions, or workflow YAML
- Wants to add testing, linting, building, or deployment automation
- Says "set up CI" or "automate my deployment"

## Workflow

### Step 1: Detect Stack & Requirements

Scan the repository for:
- **Language/Framework**: package.json (Node.js), pyproject.toml (Python), go.mod (Go), Cargo.toml (Rust), pom.xml (Java), *.csproj (C#)
- **Framework specifics**: Next.js, Django, FastAPI, Express, Spring Boot, Actix
- **Testing**: Jest, pytest, go test, cargo test, JUnit
- **Linting**: ESLint, Ruff, golangci-lint, Clippy, Checkstyle
- **Package manager**: npm, yarn, pnpm, pip, poetry, cargo, gradle
- **Deployment target**: Docker, AWS, GCP, Azure, Vercel, Fly.io, Railway
- **Existing workflows**: `.github/workflows/*.yml` to avoid conflicts

### Step 2: Generate CI Workflow (`.github/workflows/ci.yml`)

```yaml
name: CI

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main, develop]

# Cancel in-progress runs for the same branch
concurrency:
  group: ci-${{ github.ref }}
  cancel-in-progress: true

permissions:
  contents: read
  pull-requests: write

jobs:
  # ===== Lint & Type Check =====
  lint:
    name: Lint & Type Check
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'pnpm'

      - name: Install dependencies
        run: pnpm install --frozen-lockfile

      - name: Lint
        run: pnpm lint --max-warnings=0

      - name: Type check
        run: pnpm typecheck

  # ===== Test (Matrix) =====
  test:
    name: Test (Node ${{ matrix.node-version }} on ${{ matrix.os }})
    runs-on: ${{ matrix.os }}
    strategy:
      fail-fast: false
      matrix:
        node-version: ['18', '20', '22']
        os: [ubuntu-latest, windows-latest, macos-latest]
    steps:
      - uses: actions/checkout@v4

      - name: Setup Node.js ${{ matrix.node-version }}
        uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node-version }}
          cache: 'pnpm'

      - name: Install dependencies
        run: pnpm install --frozen-lockfile

      - name: Run unit tests
        run: pnpm test:unit -- --coverage

      - name: Run integration tests
        run: pnpm test:integration

      - name: Upload coverage
        if: matrix.os == 'ubuntu-latest' && matrix.node-version == '20'
        uses: codecov/codecov-action@v4
        with:
          token: ${{ secrets.CODECOV_TOKEN }}
          files: ./coverage/lcov.info

  # ===== Security Scan =====
  security:
    name: Security Scan
    runs-on: ubuntu-latest
    permissions:
      contents: read
      security-events: write
    steps:
      - uses: actions/checkout@v4

      - name: Dependency scan (audit)
        run: pnpm audit --audit-level=high
        continue-on-error: true

      - name: CodeQL Analysis
        uses: github/codeql-action/init@v3
        with:
          languages: javascript-typescript

      - name: CodeQL Autobuild
        uses: github/codeql-action/autobuild@v3

      - name: CodeQL Analysis
        uses: github/codeql-action/analyze@v3

      - name: Container scan (if Dockerfile exists)
        uses: aquasecurity/trivy-action@master
        if: hashFiles('Dockerfile') != ''
        with:
          scan-type: 'fs'
          scan-ref: '.'
          severity: 'CRITICAL,HIGH'

  # ===== Build =====
  build:
    name: Build
    runs-on: ubuntu-latest
    needs: [lint, test]
    steps:
      - uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'pnpm'

      - name: Install dependencies
        run: pnpm install --frozen-lockfile

      - name: Build
        run: pnpm build

      - name: Upload build artifacts
        uses: actions/upload-artifact@v4
        with:
          name: build-output
          path: ./dist
          retention-days: 7
```

### Step 3: Generate CD Workflow (`.github/workflows/deploy.yml`)

```yaml
name: Deploy

on:
  push:
    branches: [main]
    tags: ['v*']
  workflow_dispatch:
    inputs:
      environment:
        description: 'Deploy target'
        required: true
        default: 'staging'
        type: choice
        options:
          - staging
          - production

concurrency:
  group: deploy-${{ github.event.inputs.environment || 'staging' }}
  cancel-in-progress: false

permissions:
  contents: read
  id-token: write  # Required for OIDC auth

jobs:
  deploy:
    name: Deploy to ${{ github.event.inputs.environment || 'staging' }}
    runs-on: ubuntu-latest
    environment:
      name: ${{ github.event.inputs.environment || 'staging' }}
      url: ${{ steps.deploy.outputs.url }}
    steps:
      - uses: actions/checkout@v4

      - name: Configure AWS credentials (OIDC)
        uses: aws-actions/configure-aws-credentials@v4
        with:
          role-to-assume: ${{ secrets.AWS_DEPLOY_ROLE }}
          aws-region: ${{ vars.AWS_REGION }}

      - name: Login to ECR
        uses: aws-actions/amazon-ecr-login@v2

      - name: Build and push Docker image
        uses: docker/build-push-action@v6
        with:
          context: .
          push: true
          tags: |
            ${{ vars.ECR_REGISTRY }}/${{ vars.IMAGE_NAME }}:latest
            ${{ vars.ECR_REGISTRY }}/${{ vars.IMAGE_NAME }}:${{ github.sha }}
          cache-from: type=gha
          cache-to: type=gha,mode=max

      - name: Deploy to ECS
        id: deploy
        run: |
          aws ecs update-service \
            --cluster ${{ vars.ECS_CLUSTER }} \
            --service ${{ vars.ECS_SERVICE }} \
            --force-new-deployment
          echo "url=https://${{ vars.APP_DOMAIN }}" >> $GITHUB_OUTPUT

      - name: Wait for deployment to stabilize
        run: |
          aws ecs wait services-stable \
            --cluster ${{ vars.ECS_CLUSTER }} \
            --services ${{ vars.ECS_SERVICE }}

      - name: Notify Slack on failure
        if: failure()
        uses: slackapi/slack-github-action@v1
        with:
          slack-message: "🚨 Deployment to ${{ github.event.inputs.environment }} failed: ${{ github.run_id }}"
        env:
          SLACK_WEBHOOK_URL: ${{ secrets.SLACK_WEBHOOK }}
```

### Step 4: Generate Release Workflow (`.github/workflows/release.yml`)

```yaml
name: Release

on:
  push:
    tags: ['v*']

permissions:
  contents: write

jobs:
  release:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Generate changelog
        id: changelog
        run: |
          PREV_TAG=$(git describe --tags --abbrev=0 HEAD^ 2>/dev/null || echo "")
          if [ -z "$PREV_TAG" ]; then
            CHANGELOG=$(git log --pretty=format:"- %s" HEAD)
          else
            CHANGELOG=$(git log --pretty=format:"- %s" ${PREV_TAG}..HEAD)
          fi
          echo "changelog<<EOF" >> $GITHUB_OUTPUT
          echo "$CHANGELOG" >> $GITHUB_OUTPUT
          echo "EOF" >> $GITHUB_OUTPUT

      - name: Create GitHub Release
        uses: softprops/action-gh-release@v2
        with:
          body: |
            ## Changes
            ${{ steps.changelog.outputs.changelog }}
          generate_release_notes: true
          draft: false
          prerelease: ${{ contains(github.ref, '-rc') || contains(github.ref, '-beta') }}
```

### Step 5: Generate Required Secrets & Variables Checklist

```markdown
## Required GitHub Secrets & Variables

### Secrets (encrypted)
| Name | Used by | Description |
|------|---------|-------------|
| `CODECOV_TOKEN` | ci.yml | Code coverage upload token |
| `AWS_DEPLOY_ROLE` | deploy.yml | IAM role ARN for OIDC deployment |
| `SLACK_WEBHOOK` | deploy.yml | Slack notification webhook |

### Variables (plaintext)
| Name | Default | Description |
|------|---------|-------------|
| `AWS_REGION` | us-east-1 | AWS deployment region |
| `ECR_REGISTRY` | - | ECR registry URL |
| `IMAGE_NAME` | - | Docker image name |
| `ECS_CLUSTER` | - | ECS cluster name |
| `ECS_SERVICE` | - | ECS service name |
| `APP_DOMAIN` | - | Application domain URL |

### GitHub Environments
Create environments in Settings → Environments:
1. `staging` — auto-deploy on push to main
2. `production` — manual approval required
```

## Output Constraints

- All workflows must use action versions pinned to major version (`@v4` not `@main`)
- Must include `concurrency` to cancel stale runs
- Must use OIDC for cloud auth (no long-lived access keys)
- Must set `permissions` block (never use `permissions: write-all`)
- Deployment jobs must use GitHub Environments for approval gates
- All secrets must be referenced via `secrets.*`, never hardcoded
- Include `continue-on-error` only for non-blocking steps (like audit)

## What This Skill Does NOT Do

- Does not create AWS/GCP/Azure infrastructure (generates workflow only)
- Does not manage Terraform or IaC (use DevOps skill)
- Does not handle GitLab CI, CircleCI, or Jenkins (GitHub Actions only)
- Does not run the workflows (generates YAML only)
