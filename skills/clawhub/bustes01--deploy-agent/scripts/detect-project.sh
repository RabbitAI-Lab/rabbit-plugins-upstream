#!/usr/bin/env bash
# detect-project.sh - Auto-detect project type and framework
# Usage: detect-project.sh <project-dir>
set -euo pipefail

PROJECT_DIR="${1:-.}"
cd "$PROJECT_DIR"

# ── Result (printed to stdout as key=value pairs) ──
detect() {
    local type="unknown"
    local framework=""
    local build_cmd=""
    local run_cmd=""
    local port=""
    local entrypoint=""

    # Priority 1: Explicit Docker files
    if [ -f "Dockerfile" ]; then
        type="docker"
        framework="has-dockerfile"
    fi

    for compose_file in docker-compose.yml docker-compose.yaml compose.yml compose.yaml; do
        if [ -f "$compose_file" ]; then
            type="docker-compose"
            framework="has-compose"
            break
        fi
    done

    # ── Node.js ──
    if [ -f "package.json" ] && [ "$type" = "unknown" ]; then
        type="node"
        if [ -f "yarn.lock" ]; then framework="node-yarn"; build_cmd="yarn install --frozen-lockfile"
        elif [ -f "pnpm-lock.yaml" ]; then framework="node-pnpm"; build_cmd="pnpm install --frozen-lockfile"
        elif [ -f "bun.lockb" ]; then framework="node-bun"; build_cmd="bun install"
        else framework="node-npm"; build_cmd="npm ci"; fi

        # Detect framework-specific
        if [ -f "next.config.js" ] || [ -f "next.config.mjs" ] || [ -f "next.config.ts" ]; then
            framework="${framework}-next"
            [ -f "next.config.ts" ] && framework="${framework}-ts"
            build_cmd="$build_cmd && npm run build"
            run_cmd="npm start"; port="3000"
        elif [ -f "nuxt.config.js" ] || [ -f "nuxt.config.ts" ]; then
            framework="${framework}-nuxt"
            build_cmd="$build_cmd && npm run build"
            run_cmd="npm start"; port="3000"
        elif [ -f "astro.config.mjs" ] || [ -f "astro.config.ts" ]; then
            framework="${framework}-astro"
            build_cmd="$build_cmd && npm run build"
            run_cmd="npm start"; port="4321"
        elif grep -q '"express"' package.json 2>/dev/null; then
            framework="${framework}-express"
            run_cmd="node server.js"; port="3000"
        elif grep -q '"fastify"' package.json 2>/dev/null; then
            framework="${framework}-fastify"
            run_cmd="node server.js"; port="3000"
        elif grep -q '"nest"' package.json 2>/dev/null; then
            framework="${framework}-nestjs"
            build_cmd="$build_cmd && npm run build"
            run_cmd="node dist/main"; port="3000"
        elif grep -q '"@sveltejs/kit"' package.json 2>/dev/null; then
            framework="${framework}-sveltekit"
            build_cmd="$build_cmd && npm run build"
            run_cmd="npm start"; port="5173"
        elif [ -f "vite.config.js" ] || [ -f "vite.config.ts" ]; then
            framework="${framework}-vite"
            build_cmd="$build_cmd && npm run build"
            run_cmd="npx serve dist"; port="4173"
        else
            # Try to guess entry from scripts or package.json main
            local main_script
            main_script=$(node -e "try{const p=require('./package.json');console.log(p.main||p.bin?Object.values(p.bin)[0]||'':'')}catch(e){}" 2>/dev/null || true)
            [ -z "$main_script" ] && main_script="index.js"
            [ -f "$main_script" ] && run_cmd="node $main_script" || run_cmd="npm start"
            port=$(node -e "try{const p=require('./package.json');const s=p.scripts||{};const m=s.start||'';const match=m.match(/--port\s*(\d+)/);console.log(match?match[1]:'')}catch(e){}" 2>/dev/null || echo "")
            [ -z "$port" ] && port="3000"
        fi
    fi

    # ── Python ──
    if [ -f "requirements.txt" ] || [ -f "Pipfile" ] || [ -f "pyproject.toml" ] || [ -f "setup.py" ] && [ "$type" = "unknown" ]; then
        type="python"
        if [ -f "Pipfile" ]; then framework="python-pipenv"
        elif [ -f "pyproject.toml" ]; then
            if grep -q "poetry" pyproject.toml 2>/dev/null; then framework="python-poetry"
            else framework="python-pdm"; fi
        else framework="python-pip"; fi

        # Detect web framework
        if [ -f "manage.py" ]; then
            framework="${framework}-django"
            build_cmd=""; run_cmd="python manage.py runserver 0.0.0.0:\$PORT"
            port="8000"
        elif [ -f "app.py" ] && grep -q "Flask\|flask" app.py 2>/dev/null; then
            framework="${framework}-flask"
            run_cmd="python app.py"; port="5000"
        elif grep -q "fastapi\|FastAPI" main.py app.py 2>/dev/null; then
            framework="${framework}-fastapi"
            run_cmd="uvicorn main:app --host 0.0.0.0 --port \$PORT"
            port="8000"
        else
            run_cmd="python main.py" || run_cmd="python app.py"
            port="8000"
        fi
    fi

    # ── Go ──
    if [ -f "go.mod" ] && [ "$type" = "unknown" ]; then
        type="go"
        local go_file
        go_file=$(grep -rl 'func main' *.go 2>/dev/null | head -1) || true
        [ -z "$go_file" ] && go_file=$(find . -maxdepth 2 -name '*.go' -exec grep -l 'func main' {} \; 2>/dev/null | head -1) || true
        framework="go"
        build_cmd="go build -o /app/app ."
        run_cmd="/app/app"
        port="8080"
    fi

    # ── Rust ──
    if [ -f "Cargo.toml" ] && [ "$type" = "unknown" ]; then
        type="rust"
        framework="rust"
        build_cmd="cargo build --release"
        run_cmd="./target/release/$(grep -E '^name\s*=' Cargo.toml | head -1 | sed 's/.*= *"\(.*\)"/\1/')"
        port="8080"
    fi

    # ── Static HTML ──
    if [ -f "index.html" ] && [ "$type" = "unknown" ]; then
        type="static"
        framework="static-html"
        build_cmd=""
        run_cmd=""
        port="80"
    fi

    # ── Java ──
    if [ -f "pom.xml" ] && [ "$type" = "unknown" ]; then
        type="java"
        framework="java-maven"
        build_cmd="mvn clean package -DskipTests"
        run_cmd="java -jar target/*.jar"
        port="8080"
    fi
    if [ -f "build.gradle" ] || [ -f "build.gradle.kts" ] && [ "$type" = "unknown" ]; then
        type="java"
        framework="java-gradle"
        build_cmd="gradle build -x test"
        run_cmd="java -jar build/libs/*.jar"
        port="8080"
    fi

    # ── Ruby on Rails ──
    if [ -f "Gemfile" ] && [ "$type" = "unknown" ]; then
        type="ruby"
        if [ -f "config/application.rb" ] && grep -q "Rails" config/application.rb 2>/dev/null; then
            framework="rails"
            build_cmd="bundle install && rails assets:precompile"
            run_cmd="rails server -b 0.0.0.0 -p \$PORT"
            port="3000"
        else
            framework="ruby"
            build_cmd="bundle install"
            run_cmd="ruby app.rb"
            port="4567"
        fi
    fi

    # ── PHP ──
    if [ -f "composer.json" ] && [ "$type" = "unknown" ]; then
        type="php"
        framework="php-laravel"
        build_cmd="composer install --no-dev"
        run_cmd="php artisan serve --host=0.0.0.0 --port=\$PORT"
        port="8000"
    fi

    # ── Deno ──
    if [ -f "deno.json" ] || [ -f "deno.jsonc" ] && [ "$type" = "unknown" ]; then
        type="deno"
        framework="deno"
        local main_file
        main_file=$(deno eval "try{const d=JSON.parse(await Deno.readTextFile('deno.json'));console.log(d.tasks?.start||d.main||'main.ts')}catch(e){}" 2>/dev/null || echo "main.ts")
        run_cmd="deno run --allow-all $main_file"
        port="8000"
    fi

    # Output as key=value pairs
    echo "TYPE=$type"
    echo "FRAMEWORK=$framework"
    echo "BUILD_CMD=$build_cmd"
    echo "RUN_CMD=$run_cmd"
    echo "PORT=$port"
    echo "ENTRYPOINT=$entrypoint"
    echo ""
    # Human readable
    echo "[DETECT] Project type: $type"
    echo "[DETECT] Framework: $framework"
    [ -n "$build_cmd" ] && echo "[DETECT] Build: $build_cmd"
    [ -n "$run_cmd" ] && echo "[DETECT] Run: $run_cmd"
    [ -n "$port" ] && echo "[DETECT] Default port: $port"
}

detect
