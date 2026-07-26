#!/usr/bin/env python3
"""
JSON Python Code Executor Skill
Version: 1.0.0
Description: Parse nested JSON and execute Python code in isolated processes
"""
import json
import sys
import os
import argparse
import subprocess
import tempfile
import time
from typing import Any, Dict, Optional, List
from multiprocessing import Process, Queue


class Skill:
    def __init__(self):
        self.name = "json-python-executor"
        self.version = "1.0.0"
        self.description = "Parse JSON and execute Python code"

    def execute(self, **kwargs) -> Dict[str, Any]:
        raise NotImplementedError("子类必须实现execute方法")

    def validate_inputs(self, **kwargs) -> bool:
        return True

    def get_metadata(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "version": self.version,
            "description": self.description,
            "author": "Your Name",
            "created": "2026-07-02",
        }


class JSONCodeExecutorSkill(Skill):
    def __init__(self):
        super().__init__()
        self.description = "解析多层嵌套JSON，识别并执行Python代码"

    def execute(
        self,
        input_file: str,
        output_file: Optional[str] = None,
        timeout: int = 300,
        detach: bool = True,
    ) -> Dict[str, Any]:
        if not os.path.exists(input_file):
            return {"status": "failed", "error": f"文件不存在: {input_file}"}

        result = self._process_json(input_file, output_file, timeout, detach)
        return {
            "status": "success",
            "executed": result.get("total_executed", 0),
            "failed": result.get("total_failed", 0),
            "process_ids": result.get("process_ids", []),
        }

    def _process_json(
        self, input_file: str, output_file: Optional[str], timeout: int, detach: bool
    ) -> Dict[str, Any]:
        try:
            with open(input_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            if not isinstance(data, list):
                return {
                    "total_executed": 0,
                    "total_failed": 0,
                    "process_ids": [],
                    "error": "JSON根节点必须是数组"
                }
            
            executed_count = 0
            failed_count = 0
            process_ids = []
            results = []
            
            for idx, item in enumerate(data):
                if not isinstance(item, dict):
                    continue
                
                python_code = item.get('python_code')
                if not python_code or not isinstance(python_code, str):
                    continue
                
                item_id = item.get('id', idx)
                item_label = item.get('label', f'item_{idx}')
                
                try:
                    if detach:
                        pid = self._execute_detached(python_code, item_id, item_label)
                        if pid:
                            process_ids.append(pid)
                            executed_count += 1
                            results.append({
                                "id": item_id,
                                "label": item_label,
                                "status": "detached",
                                "pid": pid
                            })
                    else:
                        result = self._execute_sync(python_code, item_id, item_label, timeout)
                        if result.get('success'):
                            executed_count += 1
                        else:
                            failed_count += 1
                        results.append({
                            "id": item_id,
                            "label": item_label,
                            "status": "completed" if result.get('success') else "failed",
                            "output": result.get('output', ''),
                            "error": result.get('error', '')
                        })
                        
                except Exception as e:
                    failed_count += 1
                    results.append({
                        "id": item_id,
                        "label": item_label,
                        "status": "error",
                        "error": str(e)
                    })
            
            if output_file:
                with open(output_file, 'w', encoding='utf-8') as f:
                    json.dump({
                        "total_executed": executed_count,
                        "total_failed": failed_count,
                        "process_ids": process_ids,
                        "results": results,
                        "timestamp": time.time()
                    }, f, indent=2, ensure_ascii=False)
            
            return {
                "total_executed": executed_count,
                "total_failed": failed_count,
                "process_ids": process_ids,
                "results": results
            }
            
        except json.JSONDecodeError as e:
            return {
                "total_executed": 0,
                "total_failed": 0,
                "process_ids": [],
                "error": f"JSON解析失败: {str(e)}"
            }
        except Exception as e:
            return {
                "total_executed": 0,
                "total_failed": 0,
                "process_ids": [],
                "error": f"处理失败: {str(e)}"
            }

    def _execute_detached(self, python_code: str, item_id: int, label: str) -> Optional[int]:
        try:
            temp_file = tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False)
            temp_file.write(python_code)
            temp_file.close()
            
            process = subprocess.Popen(
                [sys.executable, temp_file.name],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                stdin=subprocess.DEVNULL,
                start_new_session=True
            )
            
            time.sleep(0.1)
            
            if process.poll() is None:
                return process.pid
            else:
                os.unlink(temp_file.name)
                return None
                
        except Exception:
            return None

    def _execute_sync(self, python_code: str, item_id: int, label: str, timeout: int) -> Dict[str, Any]:
        try:
            temp_file = tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False)
            temp_file.write(python_code)
            temp_file.close()
            
            try:
                result = subprocess.run(
                    [sys.executable, temp_file.name],
                    capture_output=True,
                    text=True,
                    timeout=timeout
                )
                
                return {
                    "success": result.returncode == 0,
                    "output": result.stdout,
                    "error": result.stderr if result.returncode != 0 else ""
                }
            finally:
                try:
                    os.unlink(temp_file.name)
                except:
                    pass
                
        except subprocess.TimeoutExpired:
            return {
                "success": False,
                "output": "",
                "error": f"执行超时 ({timeout}秒)"
            }
        except Exception as e:
            return {
                "success": False,
                "output": "",
                "error": str(e)
            }


def main():
    skill = JSONCodeExecutorSkill()

    parser = argparse.ArgumentParser(description=skill.description)
    parser.add_argument("-i", "--input", required=True, help="输入JSON文件")
    parser.add_argument("-o", "--output", help="输出JSON文件")
    parser.add_argument("--timeout", type=int, default=300, help="超时时间")
    parser.add_argument("--wait", action="store_true", help="等待子进程")

    args = parser.parse_args()

    result = skill.execute(
        input_file=args.input,
        output_file=args.output,
        timeout=args.timeout,
        detach=not args.wait,
    )

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()