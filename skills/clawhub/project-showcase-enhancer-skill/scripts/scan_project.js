/**
 * 项目快速扫描器 — 硬编码字典 + 结构化输出
 * 用法: node scan_project.js <项目目录> [--max-depth N]
 * 输出: JSON 到 stdout，供 LLM 消费做深度分析
 */
const fs = require('fs');
const path = require('path');

// ── 技术栈标志文件映射 ──────────────────────────────
const TECH_FLAGS = {
  'package.json':         { stack: 'Node.js', type: 'runtime' },
  'package-lock.json':    { stack: 'npm', type: 'lock' },
  'yarn.lock':            { stack: 'Yarn', type: 'lock' },
  'pnpm-lock.yaml':       { stack: 'pnpm', type: 'lock' },
  'tsconfig.json':        { stack: 'TypeScript', type: 'tool' },
  'jsconfig.json':        { stack: 'JavaScript (JSConfig)', type: 'tool' },
  'vite.config.js':       { stack: 'Vite', type: 'build' },
  'vite.config.ts':       { stack: 'Vite (TypeScript)', type: 'build' },
  'webpack.config.js':    { stack: 'Webpack', type: 'build' },
  'vue.config.js':        { stack: 'Vue CLI', type: 'build' },
  'next.config.js':       { stack: 'Next.js', type: 'framework' },
  'next.config.mjs':      { stack: 'Next.js (ESM)', type: 'framework' },
  'next.config.ts':       { stack: 'Next.js (TypeScript)', type: 'framework' },
  'nuxt.config.js':       { stack: 'Nuxt.js', type: 'framework' },
  'nuxt.config.ts':       { stack: 'Nuxt.js (TypeScript)', type: 'framework' },
  'svelte.config.js':     { stack: 'SvelteKit', type: 'framework' },
  'astro.config.mjs':     { stack: 'Astro', type: 'framework' },
  'tailwind.config.js':   { stack: 'Tailwind CSS', type: 'css' },
  'tailwind.config.ts':   { stack: 'Tailwind CSS (TypeScript)', type: 'css' },
  'postcss.config.js':    { stack: 'PostCSS', type: 'css' },
  'eslint.config.js':     { stack: 'ESLint', type: 'lint' },
  'eslint.config.mjs':    { stack: 'ESLint (ESM)', type: 'lint' },
  '.eslintrc.js':         { stack: 'ESLint', type: 'lint' },
  '.eslintrc.json':       { stack: 'ESLint', type: 'lint' },
  'prettier.config.js':   { stack: 'Prettier', type: 'lint' },
  '.prettierrc':          { stack: 'Prettier', type: 'lint' },
  'go.mod':               { stack: 'Go', type: 'runtime' },
  'pom.xml':              { stack: 'Java (Maven)', type: 'build' },
  'build.gradle':         { stack: 'Java (Gradle)', type: 'build' },
  'build.gradle.kts':     { stack: 'Java/Kotlin (Gradle KTS)', type: 'build' },
  'settings.gradle':      { stack: 'Gradle', type: 'build' },
  'requirements.txt':     { stack: 'Python (pip)', type: 'runtime' },
  'pyproject.toml':       { stack: 'Python', type: 'build' },
  'Pipfile':              { stack: 'Python (Pipenv)', type: 'runtime' },
  'Cargo.toml':           { stack: 'Rust', type: 'build' },
  'CMakeLists.txt':       { stack: 'C/C++ (CMake)', type: 'build' },
  'Makefile':             { stack: 'Make', type: 'build' },
  'Dockerfile':           { stack: 'Docker', type: 'deploy' },
  'docker-compose.yml':   { stack: 'Docker Compose', type: 'deploy' },
  'docker-compose.yaml':  { stack: 'Docker Compose', type: 'deploy' },
  '.github/workflows':    { stack: 'GitHub Actions', type: 'ci' },
  '.gitlab-ci.yml':       { stack: 'GitLab CI', type: 'ci' },
  'nginx.conf':           { stack: 'Nginx', type: 'deploy' },
  'jest.config.js':       { stack: 'Jest', type: 'test' },
  'jest.config.ts':       { stack: 'Jest (TypeScript)', type: 'test' },
  'vitest.config.ts':     { stack: 'Vitest', type: 'test' },
  'playwright.config.ts': { stack: 'Playwright', type: 'test' },
  'cypress.config.ts':    { stack: 'Cypress', type: 'test' },
  'prisma':               { stack: 'Prisma', type: 'orm' },
  'drizzle.config.ts':    { stack: 'Drizzle ORM', type: 'orm' },
  'ormconfig.json':       { stack: 'TypeORM', type: 'orm' },
};

// ── 目录职责映射 ────────────────────────────────────
const DIR_ROLES = {
  'src':           '核心源代码',
  'app':           '应用主目录 (Next.js / 后端)',
  'pages':         '页面路由目录',
  'components':    'UI 组件目录',
  'layouts':       '布局组件目录',
  'composables':   'Vue 组合式函数',
  'hooks':         'React Hooks 目录',
  'stores':        '状态管理目录',
  'store':         '状态管理目录',
  'services':      '业务服务层',
  'api':           'API 接口层',
  'routes':        '路由定义目录',
  'controllers':   '控制器目录',
  'models':        '数据模型目录',
  'entities':      'ORM 实体目录',
  'repositories':  '数据访问层',
  'middlewares':   '中间件目录',
  'middleware':    '中间件目录',
  'utils':         '工具函数目录',
  'helpers':       '辅助函数目录',
  'lib':           '核心库目录',
  'config':        '配置文件目录',
  'constants':     '常量定义目录',
  'types':         'TypeScript 类型定义',
  'interfaces':    '接口定义目录',
  'enums':         '枚举定义目录',
  'assets':        '静态资源目录',
  'public':        '公共静态资源',
  'static':        '静态文件目录',
  'styles':        '样式文件目录',
  'css':           'CSS 样式目录',
  'tests':         '测试用例目录',
  'test':          '测试用例目录',
  '__tests__':     '测试用例目录',
  'spec':          '测试规格目录',
  'e2e':           '端到端测试',
  'mocks':         'Mock 数据目录',
  'fixtures':      '测试夹具目录',
  'scripts':       '工具脚本目录',
  'bin':           '可执行脚本目录',
  'docs':          '文档目录',
  'database':      '数据库相关目录',
  'migrations':    '数据库迁移目录',
  'seeds':         '数据库种子数据',
  'dist':          '构建输出目录',
  'build':         '构建输出目录',
  'out':           '构建输出目录',
  'node_modules':  'Node.js 依赖',
  'venv':          'Python 虚拟环境',
  '.git':          'Git 仓库',
  '.next':         'Next.js 构建缓存',
  '.nuxt':         'Nuxt.js 构建缓存',
};

// ── 入口文件模式 ────────────────────────────────────
const ENTRY_PATTERNS = [
  /^(index|main|app|server|startup|bootstrap)\.(js|mjs|ts|tsx|jsx|py|go|rs|java)$/i,
  /^src\/(index|main|app|server)\.(js|mjs|ts|tsx|jsx|py)$/i,
  /^src\/main\.(java|kt)$/i,
  /^pages\/_app\.(tsx|jsx|js|ts)$/i,
];

// ── 配置文件模式 ────────────────────────────────────
const CONFIG_PATTERNS = [
  '.env', '.env.local', '.env.development', '.env.production',
  '.env.example', '.env.template',
  'application.yml', 'application.yaml', 'application.properties',
  'application-dev.yml', 'application-prod.yml',
  'bootstrap.yml', 'appsettings.json',
  '.editorconfig', '.gitignore', '.dockerignore',
];

// ── 主逻辑 ──────────────────────────────────────────

class ProjectScanner {
  constructor(projectPath, maxDepth = 5) {
    this.projectPath = path.resolve(projectPath);
    this.maxDepth = maxDepth;
    this.result = {
      projectName: path.basename(this.projectPath),
      projectPath: this.projectPath,
      scannedAt: new Date().toISOString(),
      techStack: {
        runtime: [],
        framework: [],
        build: [],
        css: [],
        test: [],
        orm: [],
        lint: [],
        deploy: [],
        ci: [],
        other: [],
      },
      dependencies: {},
      directoryStructure: [],
      entryFiles: [],
      configFiles: [],
      fileStats: { total: 0, byExtension: {} },
      readmeContent: '',
      packageJson: null,
      warnings: [],
    };
  }

  async scan() {
    await Promise.all([
      this.scanRootFlags(),
      this.scanDirectory(this.projectPath, 0),
      this.extractReadme(),
      this.extractPackageJson(),
    ]);
    return this.result;
  }

  // 扫描根目录识别技术栈标志文件
  async scanRootFlags() {
    let entries;
    try {
      entries = await fs.promises.readdir(this.projectPath);
    } catch (e) {
      this.result.warnings.push(`无法读取项目目录: ${e.message}`);
      return;
    }

    for (const name of entries) {
      const info = TECH_FLAGS[name];
      if (!info) continue;

      // 分类到对应槽位
      if (this.result.techStack[info.type]) {
        this.result.techStack[info.type].push(info.stack);
      } else {
        this.result.techStack.other.push(info.stack);
      }

      // 特殊处理：检查子文件夹（如 .github/workflows）
      if (name === '.github') {
        try {
          const subEntries = await fs.promises.readdir(path.join(this.projectPath, name));
          for (const sub of subEntries) {
            const key = `${name}/${sub}`;
            if (TECH_FLAGS[key]) {
              const si = TECH_FLAGS[key];
              if (this.result.techStack[si.type]) {
                this.result.techStack[si.type].push(si.stack);
              }
            }
          }
        } catch (_) {}
      }
    }
  }

  // 递归扫描目录结构
  async scanDirectory(basePath, depth) {
    if (depth > this.maxDepth) return;

    let entries;
    try {
      entries = await fs.promises.readdir(basePath, { withFileTypes: true });
    } catch (e) {
      return;
    }

    for (const entry of entries) {
      // 跳过隐藏文件和常见忽略目录
      if (entry.name.startsWith('.') || entry.name === 'node_modules' ||
          entry.name === 'venv' || entry.name === '__pycache__' ||
          entry.name === '.next' || entry.name === '.nuxt' ||
          entry.name === 'dist' || entry.name === 'build' ||
          entry.name === 'target' || entry.name === 'coverage') {
        continue;
      }

      const fullPath = path.join(basePath, entry.name);
      const relativePath = path.relative(this.projectPath, fullPath);

      if (entry.isDirectory()) {
        const role = DIR_ROLES[entry.name] || null;
        this.result.directoryStructure.push({
          path: relativePath,
          depth,
          role: role,
        });
        await this.scanDirectory(fullPath, depth + 1);
      } else if (entry.isFile()) {
        this.result.fileStats.total++;
        const ext = path.extname(entry.name).toLowerCase();
        this.result.fileStats.byExtension[ext] =
          (this.result.fileStats.byExtension[ext] || 0) + 1;

        // 检测入口文件
        if (ENTRY_PATTERNS.some(p => p.test(relativePath))) {
          this.result.entryFiles.push({
            path: relativePath,
            size: this.tryGetSize(fullPath),
          });
        }

        // 检测配置文件
        if (CONFIG_PATTERNS.some(p => {
          if (p === entry.name) return true;
          if (p.includes('/') && relativePath === p) return true;
          return false;
        })) {
          this.result.configFiles.push(relativePath);
        }
      }
    }
  }

  // 读取 README
  async extractReadme() {
    const readmeNames = ['README.md', 'readme.md', 'README.MD', 'README.txt'];
    for (const name of readmeNames) {
      try {
        const p = path.join(this.projectPath, name);
        if (fs.existsSync(p)) {
          const content = await fs.promises.readFile(p, 'utf-8');
          this.result.readmeContent = content.slice(0, 5000); // 最多 5000 字符
          return;
        }
      } catch (_) {}
    }
  }

  // 读取 package.json
  async extractPackageJson() {
    try {
      const p = path.join(this.projectPath, 'package.json');
      if (fs.existsSync(p)) {
        const raw = await fs.promises.readFile(p, 'utf-8');
        const pkg = JSON.parse(raw);
        this.result.packageJson = {
          name: pkg.name || '',
          version: pkg.version || '',
          description: pkg.description || '',
          license: pkg.license || '',
          scripts: Object.keys(pkg.scripts || {}),
        };
        // 合并所有依赖
        const deps = { ...(pkg.dependencies || {}), ...(pkg.devDependencies || {}) };
        this.result.dependencies = deps;
      }
    } catch (e) {
      this.result.warnings.push(`package.json 解析失败: ${e.message}`);
    }
  }

  tryGetSize(filePath) {
    try { return fs.statSync(filePath).size; } catch (_) { return 0; }
  }
}

// ── 入口 ────────────────────────────────────────────

async function main() {
  const args = process.argv.slice(2);
  if (args.length < 1) {
    console.error('用法: node scan_project.js <项目目录> [--max-depth N]');
    process.exit(1);
  }

  let projectPath = args[0];
  let maxDepth = 5;

  for (let i = 1; i < args.length; i++) {
    if (args[i] === '--max-depth' && args[i + 1]) {
      maxDepth = parseInt(args[i + 1], 10);
      i++;
    }
  }

  // 支持相对路径
  if (!path.isAbsolute(projectPath)) {
    projectPath = path.resolve(projectPath);
  }

  const scanner = new ProjectScanner(projectPath, maxDepth);
  const result = await scanner.scan();
  console.log(JSON.stringify(result, null, 2));
}

// 导出供编程调用
module.exports = { ProjectScanner, TECH_FLAGS, DIR_ROLES, ENTRY_PATTERNS, CONFIG_PATTERNS };

if (require.main === module) {
  main().catch(err => {
    console.error(`扫描失败: ${err.message}`);
    process.exit(1);
  });
}
