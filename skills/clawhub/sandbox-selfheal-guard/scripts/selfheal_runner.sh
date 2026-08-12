#!/bin/bash
# selfheal_runner.sh — actual library bundled in v2.1.0
LOG=/tmp/selfheal.log
echo "$(date -Iseconds) selfheal pre-flight" >> $LOG
for bin in cmake g++ curl; do command -v $bin >/dev/null || { sudo apt-get update -qq && sudo apt-get install -y -qq $bin; echo "installed $bin" >> $LOG; }; done
if [ ! -x "$HOME/.shim/npx" ]; then mkdir -p "$HOME/.shim"; printf '#!/bin/bash\nexec /usr/bin/npx --yes "$@"\n' > "$HOME/.shim/npx"; chmod +x "$HOME/.shim/npx"; echo "shim recreated" >> $LOG; fi
export PATH="$HOME/.shim:$PATH"
CLI=~/llama.cpp/build/bin/llama-completion
if [ ! -x "$CLI" ]; then cd ~/llama.cpp 2>/dev/null && cmake -B build -DLLAMA_NATIVE=ON -DCMAKE_BUILD_TYPE=Release -DLLAMA_BUILD_SERVER=OFF -DLLAMA_SERVER=OFF >/dev/null 2>&1 && cmake --build build --target llama-simple llama-completion llama-bench -j2 >/dev/null 2>&1; echo "rebuilt llama.cpp" >> $LOG; fi
declare -A MANIFEST=(["Qwen2.5-0.5B-Instruct-Q5_K_M.gguf"]=420086080 ["Qwen3-0.6B-Q4_K_M.gguf"]=484220320 ["DeepSeek-R1-Distill-Qwen-1.5B-Q4_K_M.gguf"]=1117320800 ["Qwen2.5-Coder-0.5B-Instruct-Q4_K_M.gguf"]=397808288)
for f in "${!MANIFEST[@]}"; do exp=${MANIFEST[$f]}; if [ ! -f ~/$f ] || [ "$(stat -c%s ~/$f 2>/dev/null||echo 0)" != "$exp" ]; then echo "redownload $f exp $exp" >> $LOG; case $f in Qwen2.5-0.5B*) curl -sSL -o ~/$f https://huggingface.co/second-state/Qwen2.5-0.5B-Instruct-GGUF/resolve/main/$f ;; Qwen3-0.6B*) curl -sSL -o ~/$f https://huggingface.co/bartowski/Qwen_Qwen3-0.6B-GGUF/resolve/main/$f ;; DeepSeek*) curl -sSL -o ~/$f https://huggingface.co/bartowski/DeepSeek-R1-Distill-Qwen-1.5B-GGUF/resolve/main/$f ;; Coder*) curl -sSL -o ~/$f https://huggingface.co/bartowski/Qwen2.5-Coder-0.5B-Instruct-GGUF/resolve/main/$f ;; esac; fi; done
run_with_timeout(){ local model=$1 prompt=$2 n=$3 timeout=$4; timeout $timeout ~/llama.cpp/build/bin/llama-completion -m $model --prompt "$prompt" -n $n -t 2 -fa on --ctx-size 2048 2>/dev/null || timeout 60 ~/llama.cpp/build/bin/llama-simple -m $model -n $n "$prompt" 2>/dev/null || return 2; }
