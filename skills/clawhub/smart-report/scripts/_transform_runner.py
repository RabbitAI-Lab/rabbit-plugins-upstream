"""transform 代码沙箱子进程执行器。

父进程（data_transformer.py）在 spawn 前已完成「关键字黑名单 + AST 白名单」校验，
本脚本只负责在资源受限、受限 builtins 的子进程中执行已通过校验的代码，并把
result DataFrame 落盘回传。进程级资源限制 + 受限 builtins 构成双重保险：即使
校验存在绕过，代码也无法脱离子进程的 CPU/内存配额，且拿不到 open/exec/eval/
__import__/subprocess 等能力。
"""

import contextlib
import json
import sys

import pandas as pd
import numpy as np

# 与父进程一致的安全 builtins：禁止 open/exec/eval/__import__ 等危险能力
SAFE_BUILTINS = {
    'len': len, 'range': range, 'list': list, 'dict': dict,
    'str': str, 'int': int, 'float': float, 'bool': bool,
    'sorted': sorted, 'enumerate': enumerate, 'zip': zip,
    'map': map, 'filter': filter, 'sum': sum, 'min': min, 'max': max,
    'abs': abs, 'round': round, 'set': set, 'tuple': tuple,
    'isinstance': isinstance, 'hasattr': hasattr, 'print': print,
    'True': True, 'False': False, 'None': None,
}

# 与 exceptions.ErrorCode 对应，避免子进程 import 父包
TRANSFORM_EXEC_ERROR = 3001
TRANSFORM_NO_RESULT = 3002
TRANSFORM_INVALID_RESULT = 3003
TRANSFORM_EMPTY_RESULT = 3004


def _apply_resource_limits():
    """进程级资源限制（Unix）。Windows 无 resource 模块时静默跳过。

    限制偏保守以不误伤正常报告数据：CPU 30s（远高于 10s 墙钟超时）、
    虚拟内存 2GB（数据文件上限 100MB，正常聚合远用不到 2GB）。
    递归深度上限 500 与父进程旧实现保持一致，防递归栈溢出。
    """
    sys.setrecursionlimit(500)
    try:
        import resource
        resource.setrlimit(resource.RLIMIT_CPU, (30, 30))
        resource.setrlimit(resource.RLIMIT_AS, (2 * 1024 ** 3, 2 * 1024 ** 3))
    except (ImportError, ValueError, OSError):
        pass


def main():
    df_path, code_path, result_path, status_path = sys.argv[1:5]
    _apply_resource_limits()

    status = {'ok': False, 'code': TRANSFORM_EXEC_ERROR, 'message': ''}
    try:
        df = pd.read_pickle(df_path)
        with open(code_path, encoding='utf-8') as f:
            code = f.read()

        local_vars = {'df': df, 'pd': pd, 'np': np}
        global_vars = {'__builtins__': SAFE_BUILTINS}

        # print 重定向到 stderr：避免污染本子进程 stdout，同时失败时父进程能透传调试输出
        with contextlib.redirect_stdout(sys.stderr):
            exec(code, global_vars, local_vars)

        if 'result' not in local_vars:
            status['code'] = TRANSFORM_NO_RESULT
            status['message'] = '转换代码必须产出 result 变量'
        else:
            result = local_vars['result']
            if not isinstance(result, pd.DataFrame):
                status['code'] = TRANSFORM_INVALID_RESULT
                status['message'] = f"result 必须是 DataFrame，实际类型: {type(result).__name__}"
                status['result_type'] = type(result).__name__
            elif result.empty:
                status['code'] = TRANSFORM_EMPTY_RESULT
                status['message'] = '转换后数据为空，请检查转换逻辑'
            else:
                result.to_pickle(result_path)
                status['ok'] = True
    except Exception as e:
        status['code'] = TRANSFORM_EXEC_ERROR
        status['message'] = f'{type(e).__name__}: {e}'

    with open(status_path, 'w', encoding='utf-8') as f:
        json.dump(status, f, ensure_ascii=False)


if __name__ == '__main__':
    main()
