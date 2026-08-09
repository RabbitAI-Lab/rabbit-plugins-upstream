#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
简化版全市场股票数据更新脚本
- 移除 MCP 依赖，直接执行
- 支持 tushare（简易/全量）和 baostock（指数）
- 自动读取 DB_setting.json 和 API_tushare.txt 配置
- 默认调用 example_tushare_120（仅需 120 积分，更新股票和指数）
- 若需全量更新（需 2000+ 积分），可切换至 example_tushare_2000
"""

import os
import sys
import json
import re
import time
from datetime import datetime, timedelta

import pandas as pd
import numpy as np
import duckdb
import tushare as ts
import baostock as bs


# ========== 工具函数 ==========
def _log(phase: int, total_phases: int, message: str):
    """打印进度信息（替代 MCP 的日志）"""
    print(f"[{phase}/{total_phases}] {message}")


# ========== Updb 类（数据库操作） ==========
class Updb:
    def __init__(self, db_path=".\\Test.duckdb"):
        path = os.path.dirname(__file__)
        option_path = os.path.join(path, "DB_setting.json")
        if os.path.isfile(option_path):
            with open(option_path, 'r', encoding='utf-8') as file:
                fd: dict = json.load(file)
        else:
            fd = {}
        self.db_path = fd.get("db_path", db_path)
        self.st_tab = fd.get('stock', 'stock')
        self.st_map = fd.get("map_stock", {})
        self.id_tab = fd.get("stock_index", "stock_index")
        self.id_map = fd.get("map_stock_index", {})
        self.basic_tab = fd.get("stock_basic", "stock_basic")
        self.basic_map = fd.get("map_stock_basic", {})
        self.factor_tab = fd.get("stock_factor", "stock_factor")
        self.factor_map = fd.get("map_stock_factor", {})
        self.forecast_tab = fd.get("stock_forecast", "stock_forecast")
        self.forecast_map = fd.get("map_stock_forecast", {})
        self.dividend_tab = fd.get("stock_dividend", "stock_dividend")
        self.dividend_map = fd.get("map_stock_dividend", {})
        self.report_tab = fd.get("stock_report", "stock_report")
        self.report_map = fd.get("map_stock_report", {})

        with duckdb.connect(self.db_path) as conn:
            conn.execute("""
            CREATE TABLE IF NOT EXISTS table_date (
                table_name STRING,
                update_date DATE,
                PRIMARY KEY (table_name)
            );
            """)
            self.table_date = {"stock_forecast": None,
                               "stock_dividend": None,
                               "stock_report": None}
            rows = conn.execute(
                "SELECT table_name, update_date FROM table_date"
            ).fetchall()
            for table_name, update_date in rows:
                if table_name in self.table_date:
                    self.table_date[table_name] = update_date

        self.exist_stocks = []
        self.count_stocks = 0
        self.update_date = self.date_stock_index("000001")

    def write_table_date(self, table_name: str):
        with duckdb.connect(self.db_path) as conn:
            conn.execute(
                "INSERT OR REPLACE INTO table_date (table_name, update_date) VALUES (?, ?)",
                [table_name, self.update_date]
            )
        self.table_date[table_name] = self.update_date

    def date_stock_index(self, symbol):
        symbol = ''.join(re.findall(r'\d', symbol))
        gp_col = self.id_map.get("symbol", "symbol")
        td_col = self.id_map.get("trade_date", "trade_date")
        with duckdb.connect(self.db_path) as conn:
            last_date = conn.execute(f"SELECT MAX({td_col}) FROM {self.id_tab} "
                                      f"WHERE {gp_col}='{symbol}'").fetchone()[0]
            if last_date is None:
                last_date = conn.execute(f"SELECT MIN({td_col}) FROM {self.id_tab}").fetchone()[0]
        return last_date

    def update_stock_index(self, df: pd.DataFrame) -> str:
        try:
            col_default = ["trade_date", "symbol", "open", "high", "low", "close", "pre_close", "vol", "voe"]
            if not all(col in df.columns for col in col_default):
                return f"数据缺少必要列，必要的列名：{col_default}"
            df.loc[:, 'symbol'] = self.norm_symbol(df['symbol'])
            df['trade_date'] = df['trade_date'].astype(object)
            df.loc[:, 'trade_date'] = pd.to_datetime(df['trade_date'], errors='coerce').dt.date
            df = df.dropna(subset=['trade_date'])
            symbols = df['symbol'].unique().tolist()
            df.rename(columns=self.id_map, inplace=True)

            conn = duckdb.connect(self.db_path)
            table_columns = [row[0] for row in conn.execute(f"DESCRIBE {self.id_tab}").fetchall()]
            if not all(col in df.columns for col in table_columns):
                return f"列名不匹配：数据：{df.columns.to_list()},数据库：{table_columns}"
            df = df[table_columns]
            gp_col = self.id_map.get('symbol', 'symbol')
            for symbol in symbols:
                last_date = conn.execute(f"""
                    SELECT MAX({self.id_map.get('trade_date','trade_date')})
                    FROM {self.id_tab} WHERE {gp_col}='{symbol}';
                """).fetchone()[0]
                if last_date is None:
                    df2 = df[df[gp_col] == symbol]
                    conn.execute(f"INSERT OR REPLACE INTO {self.id_tab} SELECT * FROM df2")
                else:
                    df2 = df[df[gp_col] == symbol]
                    conn.execute(f"INSERT OR IGNORE INTO {self.id_tab} SELECT * FROM df2")
            conn.close()
            if '000001' in symbols:
                self.update_date = self.date_stock_index("000001")
            return "OK"
        except Exception as e:
            return f"更新stock_index运行异常：{e}"

    def dates_await(self, table="stock") -> list:
        conn = duckdb.connect(self.db_path)
        if table == "stock":
            td_col = self.st_map.get("trade_date", "trade_date")
            last_date = conn.execute(f"SELECT MAX({td_col}) FROM {self.st_tab}").fetchone()[0]
        elif table == "stock_factor":
            td_col = self.factor_map.get("trade_date", "trade_date")
            last_date = conn.execute(f"SELECT MAX({td_col}) FROM {self.factor_tab}").fetchone()[0]
        elif table == "stock_forecast":
            if self.table_date.get("stock_forecast"):
                last_date = self.table_date.get("stock_forecast")
            else:
                ad_col = self.forecast_map.get("ann_date", "ann_date")
                last_date = conn.execute(f"SELECT MAX({ad_col}) FROM {self.forecast_tab}").fetchone()[0]
        elif table == "stock_dividend":
            if self.table_date.get("stock_dividend"):
                last_date = self.table_date.get("stock_dividend")
            else:
                ed_col = self.dividend_map.get("ex_date", "ex_date")
                last_date = conn.execute(f"SELECT MAX({ed_col}) FROM {self.dividend_tab}").fetchone()[0]
        elif table == "stock_report":
            if self.table_date.get("stock_report"):
                last_date = self.table_date.get("stock_report")
            else:
                ad_col = self.report_map.get("ann_date", "ann_date")
                last_date = conn.execute(f"SELECT MAX({ad_col}) FROM {self.report_tab}").fetchone()[0]
        else:
            return []
        td_col_id = self.id_map.get("trade_date", "trade_date")
        if last_date is None:
            trade_days = conn.execute(f"SELECT DISTINCT {td_col_id} FROM {self.id_tab} ORDER BY {td_col_id} ASC").fetchall()
            conn.close()
            return [row[0] for row in trade_days]
        else:
            trade_days = conn.execute(f"SELECT DISTINCT {td_col_id} FROM {self.id_tab} WHERE {td_col_id} > ? ORDER BY {td_col_id} ASC", [last_date]).fetchall()
            conn.close()
            return [row[0] for row in trade_days]

    def norm_symbol(self, stock_series: pd.Series) -> pd.Series:
        s = stock_series.astype(str).str.strip()
        s = s.apply(lambda x: ''.join(re.findall(r'\d', x)))
        return s.astype('string')

    def update_stock(self, df: pd.DataFrame, ignore_check=False) -> str:
        try:
            df.loc[:, 'symbol'] = self.norm_symbol(df['symbol'])
            df['trade_date'] = df['trade_date'].astype(object)
            df.loc[:, 'trade_date'] = pd.to_datetime(df['trade_date'], errors='coerce').dt.date
            df = df.dropna(subset=['trade_date'])
            if len(df) <= 0:
                return "无符号时间格式的数据"
            df.rename(columns=self.st_map, inplace=True)
            td_col = self.st_map.get('trade_date', 'trade_date')
            gp_col = self.st_map.get('symbol', 'symbol')
            conn = duckdb.connect(self.db_path)
            table_columns = [row[0] for row in conn.execute(f"DESCRIBE {self.st_tab}").fetchall()]
            if not all(col in df.columns for col in table_columns):
                return f"列名不匹配：数据：{df.columns.to_list()},数据库：{table_columns}"
            df = df[table_columns]

            if not self.exist_stocks:
                e_stocks = conn.execute(f"""
                    WITH max_date AS (SELECT MAX({td_col}) AS last_day FROM {self.st_tab})
                    SELECT DISTINCT {gp_col} FROM {self.st_tab}
                    WHERE {td_col} = (SELECT last_day FROM max_date)
                    ORDER BY {gp_col} ASC;
                """).fetchall()
                self.exist_stocks = [row[0] for row in e_stocks]
                self.count_stocks = len(self.exist_stocks)

            if not self.exist_stocks:
                conn.execute(f"INSERT OR REPLACE INTO {self.st_tab} SELECT * FROM df")
            else:
                intersection = set(self.exist_stocks) & set(df[gp_col].to_list())
                if self.count_stocks * 0.95 > len(intersection):
                    if ignore_check:
                        conn.execute(f"INSERT OR IGNORE INTO {self.st_tab} SELECT * FROM df")
                    else:
                        return f"股票数量{len(intersection)}，缺失过多，可能有异常"
                conn.execute(f"INSERT OR IGNORE INTO {self.st_tab} SELECT * FROM df")
            conn.close()
            return "OK"
        except Exception as e:
            return f"更新stock运行异常,{e}"

    def update_stock_basic(self, df: pd.DataFrame) -> str:
        try:
            if 'symbol' not in df.columns:
                if "ts_code" in df.columns:
                    df['symbol'] = self.norm_symbol(df['ts_code'])
                else:
                    return "无symbol列,股票代码"
            else:
                df['symbol'] = self.norm_symbol(df['symbol'])
            if 'update_date' not in df.columns:
                today = datetime.now().date()
                df['update_date'] = today
            if 'list_date' in df.columns:
                df['list_date'] = df['list_date'].astype(object)
                df.loc[:, 'list_date'] = pd.to_datetime(df['list_date'], errors='coerce').dt.date
            df.rename(columns=self.basic_map, inplace=True)
            conn = duckdb.connect(self.db_path)
            table_columns = [row[0] for row in conn.execute(f"DESCRIBE {self.basic_tab}").fetchall()]
            ab_cols = list(set(df.columns.to_list()) & set(table_columns))
            df = df[ab_cols]
            col_txt = ','.join(ab_cols)
            conn.execute(f"""
                INSERT OR REPLACE INTO {self.basic_tab} ({col_txt})
                SELECT {col_txt} FROM df
            """)
            conn.close()
            return "OK"
        except Exception as e:
            return f"更新stock_basic运行异常:{e}"

    def date_stock_basic(self):
        conn = duckdb.connect(self.db_path)
        last_date = conn.execute(f"SELECT MAX(update_date) FROM {self.basic_tab};").fetchone()[0]
        conn.close()
        return last_date

    def update_stock_factor(self, df: pd.DataFrame, ignore_check: bool = False) -> str:
        try:
            df.loc[:, 'symbol'] = self.norm_symbol(df['symbol'])
            df['trade_date'] = df['trade_date'].astype(object)
            df.loc[:, 'trade_date'] = pd.to_datetime(df['trade_date'], errors='coerce').dt.date
            df = df.dropna(subset=['trade_date'])
            if len(df) <= 0:
                return "无符号日期格式的数据"
            df.rename(columns=self.factor_map, inplace=True)
            td_col = self.factor_map.get("trade_date", "trade_date")
            gp_col = self.factor_map.get("symbol", "symbol")
            conn = duckdb.connect(self.db_path)
            table_columns = [row[0] for row in conn.execute(f"DESCRIBE {self.factor_tab}").fetchall()]
            if not all(col in df.columns for col in table_columns):
                return f"列名不匹配：数据：{df.columns.to_list()},数据库：{table_columns}"
            df = df[table_columns]

            if not self.exist_stocks:
                e_stocks = conn.execute(f"""
                    WITH max_date AS (SELECT MAX({td_col}) AS last_day FROM {self.factor_tab})
                    SELECT DISTINCT {gp_col} FROM {self.factor_tab}
                    WHERE {td_col} = (SELECT last_day FROM max_date)
                    ORDER BY {gp_col} ASC;
                """).fetchall()
                self.exist_stocks = [row[0] for row in e_stocks]
                self.count_stocks = len(self.exist_stocks)
            if not self.exist_stocks:
                conn.execute(f"INSERT OR REPLACE INTO {self.factor_tab} SELECT * FROM df")
            else:
                intersection = set(self.exist_stocks) & set(df['symbol'].to_list())
                if self.count_stocks * 0.95 > len(intersection):
                    if ignore_check:
                        conn.execute(f"INSERT OR IGNORE INTO {self.factor_tab} SELECT * FROM df")
                    else:
                        return f"股票数量{len(intersection)}，缺失过多，可能有异常"
                conn.execute(f"INSERT OR IGNORE INTO {self.factor_tab} SELECT * FROM df")
            return "OK"
        except Exception as e:
            return f"更新stock_factor运行异常,{e}"

    def update_stock_forecast(self, df: pd.DataFrame, date) -> str:
        try:
            df.loc[:, 'symbol'] = self.norm_symbol(df['symbol'])
            df['end_date'] = df['end_date'].astype(object)
            df.loc[:, 'end_date'] = pd.to_datetime(df['end_date'], errors='coerce').dt.date
            df['ann_date'] = df['ann_date'].astype(object)
            df.loc[:, 'ann_date'] = pd.to_datetime(df['ann_date'], errors='coerce').dt.date
            if 'first_ann_date' in df.columns:
                df['first_ann_date'] = df['first_ann_date'].astype(object)
                df.loc[:, 'first_ann_date'] = pd.to_datetime(df['first_ann_date'],
                                                             errors='coerce').dt.date
            df = df.dropna(subset=['end_date', 'ann_date'])
            if len(df) <= 0:
                return "无符合日期格式的数据"
            df.rename(columns=self.factor_map, inplace=True)
            with duckdb.connect(self.db_path) as conn:
                table_columns = [row[0] for row in conn.execute(f"DESCRIBE {self.forecast_tab}").fetchall()]
                if not all(col in df.columns for col in table_columns):
                    return f"列名不匹配：数据：{df.columns.to_list()},数据库：{table_columns}"
                df = df[table_columns]
                exist_tab = conn.execute(f"SELECT EXISTS (SELECT 1 FROM {self.forecast_tab})").fetchone()[0]
                if exist_tab:
                    conn.execute(f"INSERT OR IGNORE INTO {self.forecast_tab} SELECT * FROM df")
                else:
                    conn.execute(f"INSERT OR REPLACE INTO {self.forecast_tab} SELECT * FROM df")
                conn.execute("""
                    INSERT OR REPLACE INTO table_date (table_name, update_date)
                    VALUES (?, ?)
                """, ["stock_forecast", self.update_date])
            return "OK"
        except Exception as e:
            return f"更新stock_forecast运行异常,{e}"

    def update_stock_dividend(self, df: pd.DataFrame, date) -> str:
        try:
            df.loc[:, 'symbol'] = self.norm_symbol(df['symbol'])
            df['end_date'] = df['end_date'].astype(object)
            df.loc[:, 'end_date'] = pd.to_datetime(df['end_date'], errors='coerce').dt.date
            df['ann_date'] = df['ann_date'].astype(object)
            df.loc[:, 'ann_date'] = pd.to_datetime(df['ann_date'], errors='coerce').dt.date
            for s in ['record_date', 'ex_date', 'pay_date', 'imp_ann_date', 'div_listdate']:
                if s in df.columns:
                    df[s] = df[s].astype(object)
                    df.loc[:, s] = pd.to_datetime(df[s], errors='coerce').dt.date
            df = df.dropna(subset=['end_date', 'ex_date'])
            if len(df) <= 0:
                return "无符合日期格式的数据"
            df.rename(columns=self.dividend_map, inplace=True)
            with duckdb.connect(self.db_path) as conn:
                table_columns = [row[0] for row in conn.execute(f"DESCRIBE {self.dividend_tab}").fetchall()]
                if not all(col in df.columns for col in table_columns):
                    return f"列名不匹配：数据：{df.columns.to_list()},数据库：{table_columns}"
                df = df[table_columns]
                exist_tab = conn.execute(f"SELECT EXISTS (SELECT 1 FROM {self.dividend_tab})").fetchone()[0]
                if exist_tab:
                    conn.execute(f"INSERT OR IGNORE INTO {self.dividend_tab} SELECT * FROM df")
                else:
                    conn.execute(f"INSERT OR REPLACE INTO {self.dividend_tab} SELECT * FROM df")
                conn.execute("""
                    INSERT OR REPLACE INTO table_date (table_name, update_date)
                    VALUES (?, ?)
                """, ["stock_dividend", self.update_date])
            return "OK"
        except Exception as e:
            return f"更新stock_dividend运行异常,{e}"

    def update_stock_report(self, df: pd.DataFrame) -> str:
        try:
            df.loc[:, 'symbol'] = self.norm_symbol(df['symbol'])
            df['end_date'] = df['end_date'].astype(object)
            df.loc[:, 'end_date'] = pd.to_datetime(df['end_date'], errors='coerce').dt.date
            df['ann_date'] = df['ann_date'].astype(object)
            df.loc[:, 'ann_date'] = pd.to_datetime(df['ann_date'], errors='coerce').dt.date
            df = df.dropna(subset=['end_date', 'ann_date'])
            if len(df) <= 0:
                return "无符合日期格式的数据"
            df.rename(columns=self.report_map, inplace=True)
            with duckdb.connect(self.db_path) as conn:
                table_columns = [row[0] for row in conn.execute(f"DESCRIBE {self.report_tab}").fetchall()]
                if not all(col in df.columns for col in table_columns):
                    return f"列名不匹配：数据：{df.columns.to_list()},数据库：{table_columns}"
                df = df[table_columns]
                conn.execute(f"INSERT OR REPLACE INTO {self.report_tab} SELECT * FROM df")
                conn.execute("""
                    INSERT OR REPLACE INTO table_date (table_name, update_date)
                    VALUES (?, ?)
                """, ["stock_report", self.update_date])
            return "OK"
        except Exception as e:
            return f"更新stock_report运行异常,{e}"

    def creat_duckdb(self, path='') -> str:
        if not path:
            path = os.path.join(os.path.dirname(__file__), 'Test.duckdb')
        if os.path.isfile(path):
            return "文件已存在，放弃执行"
        with duckdb.connect(path) as conn:
            conn.execute("""
            CREATE TABLE IF NOT EXISTS stock (
                trade_date DATE,
                symbol STRING,
                open REAL,
                high REAL,
                low REAL,
                close REAL,
                pre_close REAL,
                vol REAL,
                voe REAL,
                PRIMARY KEY (trade_date, symbol)
            );
            """)
            conn.execute("""
            CREATE TABLE IF NOT EXISTS stock_index (
                trade_date DATE,
                symbol STRING,
                open REAL,
                high REAL,
                low REAL,
                close REAL,
                pre_close REAL,
                vol REAL,
                voe REAL,
                PRIMARY KEY (trade_date, symbol)
            );
            """)
            conn.execute("""
                CREATE TABLE IF NOT EXISTS stock_basic (
                    symbol STRING,
                    name STRING,
                    update_date DATE,
                    list_date DATE,
                    act_name STRING,
                    act_ent_type STRING,
                    industry STRING,
                    com_name STRING,
                    com_id STRING,
                    chairman STRING,
                    manager STRING,
                    secretary STRING,
                    reg_capital REAL,
                    setup_date STRING,
                    province STRING,
                    city STRING,
                    introduction STRING,
                    website STRING,
                    email STRING,
                    office STRING,
                    business_scope STRING,
                    employees INTEGER,
                    main_business STRING,
                    exchange STRING,
                    concept STRING,
                    PRIMARY KEY (symbol)
                );
            """)
            conn.execute("""
                CREATE TABLE IF NOT EXISTS stock_factor (
                    symbol STRING,
                    trade_date DATE,
                    close REAL,
                    turnover_rate REAL,
                    turnover_rate_f REAL,
                    volume_ratio REAL,
                    pe REAL,
                    pe_ttm REAL,
                    pb REAL,
                    ps REAL,
                    ps_ttm REAL,
                    dv_ratio REAL,
                    dv_ttm REAL,
                    total_share REAL,
                    float_share REAL,
                    free_share REAL,
                    total_mv REAL,
                    circ_mv REAL,
                    limit_status INTEGER,
                    PRIMARY KEY (symbol, trade_date)
                );
            """)
            conn.execute("""
            CREATE TABLE IF NOT EXISTS stock_forecast (
                symbol STRING,
                end_date DATE,
                ann_date DATE,
                first_ann_date DATE,
                type STRING,
                p_change_min REAL,
                p_change_max REAL,
                net_profit_min REAL,
                net_profit_max REAL,
                last_parent_net REAL,
                summary STRING,
                change_reason STRING,
                update_flag STRING,
                PRIMARY KEY (symbol, end_date)
            );
            """)
            conn.execute("""
            CREATE TABLE IF NOT EXISTS stock_dividend (
                symbol STRING,
                end_date DATE,
                ann_date DATE,
                imp_ann_date DATE,
                record_date DATE,
                div_listdate DATE,
                ex_date DATE,
                pay_date DATE,
                div_proc STRING,
                stk_div REAL,
                stk_bo_rate REAL,
                stk_co_rate REAL,
                cash_div REAL,
                cash_div_tax REAL,
                PRIMARY KEY (symbol, end_date)
            );
            """)
            conn.execute("""
            CREATE TABLE IF NOT EXISTS stock_report (
                symbol STRING,
                end_date DATE,
                ann_date DATE,
                eps REAL,
                dt_eps REAL,
                total_revenue_ps REAL,
                revenue_ps REAL,
                capital_rese_ps REAL,
                surplus_rese_ps REAL,
                undist_profit_ps REAL,
                extra_item REAL,
                profit_dedt REAL,
                gross_margin REAL,
                current_ratio REAL,
                quick_ratio REAL,
                cash_ratio REAL,
                ar_turn REAL,
                ca_turn REAL,
                fa_turn REAL,
                assets_turn REAL,
                op_income REAL,
                ebit REAL,
                ebitda REAL,
                fcff REAL,
                fcfe REAL,
                current_exint REAL,
                noncurrent_exint REAL,
                interestdebt REAL,
                netdebt REAL,
                tangible_asset REAL,
                working_capital REAL,
                networking_capital REAL,
                invest_capital REAL,
                retained_earnings REAL,
                diluted2_eps REAL,
                bps REAL,
                ocfps REAL,
                retainedps REAL,
                cfps REAL,
                ebit_ps REAL,
                fcff_ps REAL,
                fcfe_ps REAL,
                netprofit_margin REAL,
                grossprofit_margin REAL,
                cogs_of_sales REAL,
                expense_of_sales REAL,
                profit_to_gr REAL,
                saleexp_to_gr REAL,
                adminexp_of_gr REAL,
                finaexp_of_gr REAL,
                impai_ttm REAL,
                gc_of_gr REAL,
                op_of_gr REAL,
                ebit_of_gr REAL,
                roe REAL,
                roe_waa REAL,
                roe_dt REAL,
                roa REAL,
                npta REAL,
                roic REAL,
                roe_yearly REAL,
                roa2_yearly REAL,
                debt_to_assets REAL,
                assets_to_eqt REAL,
                dp_assets_to_eqt REAL,
                ca_to_assets REAL,
                nca_to_assets REAL,
                tbassets_to_totalassets REAL,
                int_to_talcap REAL,
                eqt_to_talcapital REAL,
                currentdebt_to_debt REAL,
                longdeb_to_debt REAL,
                ocf_to_shortdebt REAL,
                debt_to_eqt REAL,
                eqt_to_debt REAL,
                eqt_to_interestdebt REAL,
                tangibleasset_to_debt REAL,
                tangasset_to_intdebt REAL,
                tangibleasset_to_netdebt REAL,
                ocf_to_debt REAL,
                turn_days REAL,
                roa_yearly REAL,
                roa_dp REAL,
                fixed_assets REAL,
                profit_to_op REAL,
                q_saleexp_to_gr REAL,
                q_gc_to_gr REAL,
                q_roe REAL,
                q_dt_roe REAL,
                q_npta REAL,
                q_ocf_to_sales REAL,
                basic_eps_yoy REAL,
                dt_eps_yoy REAL,
                cfps_yoy REAL,
                op_yoy REAL,
                ebt_yoy REAL,
                netprofit_yoy REAL,
                dt_netprofit_yoy REAL,
                ocf_yoy REAL,
                roe_yoy REAL,
                bps_yoy REAL,
                assets_yoy REAL,
                eqt_yoy REAL,
                tr_yoy REAL,
                or_yoy REAL,
                q_sales_yoy REAL,
                q_op_qoq REAL,
                equity_yoy REAL,
                PRIMARY KEY (symbol, end_date)
            );
            """)
            conn.execute("""
            CREATE TABLE IF NOT EXISTS table_date (
                table_name STRING,
                update_date DATE,
                PRIMARY KEY (table_name)
            );
            """)
        return f"数据库创建完成{path}"

    def check_report_miss(self):
        conn = duckdb.connect(self.db_path)
        df = conn.execute(f"""
                        SELECT symbol, end_date FROM {self.report_tab}
                        ORDER BY symbol, end_date
                    """).df()
        df_list = conn.execute(f"SELECT symbol, list_date FROM {self.basic_tab}").df()
        list_dict = dict(zip(df_list["symbol"], pd.to_datetime(df_list["list_date"])))
        conn.close()
        if df.empty:
            return pd.DataFrame([])
        df['end_date'] = pd.to_datetime(df["end_date"])
        min_year = df['end_date'].min().year
        max_year = df['end_date'].max().year
        standard_quarters = ["03-31", "06-30", "09-30", "12-31"]
        norm_end_date = []
        for y in range(min_year, max_year + 1):
            for q in standard_quarters:
                norm_end_date.append(pd.to_datetime(f"{y}-{q}"))
        norm_end_date = np.array(sorted(norm_end_date))
        missing_records = []
        for symbol, group in df.groupby("symbol"):
            symbol_ld = list_dict.get(symbol)
            if not symbol_ld:
                continue
            group_valid = group[group["end_date"] >= symbol_ld].copy()
            if group_valid.empty:
                continue
            s_dates = np.array(pd.to_datetime(group_valid["end_date"]).sort_values())
            s_min = s_dates.min()
            s_max = s_dates.max()
            left = np.searchsorted(norm_end_date, s_min, side="left")
            right_idx = np.searchsorted(norm_end_date, s_max, side="right")
            expected = norm_end_date[left:right_idx]
            if len(s_dates) == len(expected):
                continue
            missing = np.setdiff1d(expected, s_dates)
            for d in missing:
                missing_records.append({
                    "symbol": symbol,
                    "missing_end_date": pd.to_datetime(d).strftime("%Y-%m-%d")
                })
        missing_df = pd.DataFrame(missing_records)
        if not missing_df.empty:
            print(f"缺失报告期总数：{len(missing_df)}")
            print(missing_df)
        else:
            print("所有股票期间完整，无中间缺失！")
        return missing_df


# ========== 更新函数（同步版本） ==========
def example_tushare_2000(api: str = '你的API', DB_path: str = '', ignore_check: bool = False):
    TOTAL_PHASES = 7
    if datetime.now().hour < 15:
        today = datetime.now().date() - timedelta(days=1)
    else:
        today = datetime.now().date()
    if today.weekday() == 6:
        today = today - timedelta(days=2)
    elif today.weekday() == 5:
        today = today - timedelta(days=1)

    today_s = today.strftime('%Y%m%d')
    updb = Updb(DB_path)
    pro = ts.pro_api(api)

    # 1. 更新指数
    _log(1, TOTAL_PHASES, "开始更新指数数据")
    id_list = ["399001.SZ", "000001.SH"]
    t0 = time.time()
    for i, ts_code in enumerate(id_list):
        start_date = updb.date_stock_index(ts_code)
        if start_date is None:
            start_date = today - timedelta(days=730)
            start_date_s = start_date.strftime('%Y%m%d')
        else:
            if today <= start_date:
                continue
            start_date_s = start_date.strftime('%Y%m%d')
        df_date = pro.index_daily(ts_code=ts_code,
                                  start_date=start_date_s,
                                  end_date=today_s)
        if len(df_date) > 0:
            df_date.rename(columns={"ts_code": "symbol", "amount": "voe"}, inplace=True)
            df_date = df_date.sort_values(by='trade_date', ignore_index=True)
            err = updb.update_stock_index(df_date)
            _log(1, TOTAL_PHASES, f"指数 {ts_code}: {err}")
        if (i + 1) % 10 == 0:
            sl_time = 10 - time.time() + t0
            if sl_time > 0:
                time.sleep(sl_time)
            t0 = time.time()
    _log(1, TOTAL_PHASES, "指数数据更新完成")
    updb.update_date = updb.date_stock_index("000001")

    # 2. 更新股票日线
    dates_id = updb.dates_await("stock")
    if not dates_id:
        _log(2, TOTAL_PHASES, "股票数据已是最新，无需更新")
    else:
        _log(2, TOTAL_PHASES, f"开始更新股票行情，共 {len(dates_id)} 个交易日待更新")
        t0 = time.time()
        for i, date in enumerate(dates_id):
            date_s = date.strftime('%Y%m%d')
            df_date = pro.daily(trade_date=date_s)
            if len(df_date) > 0:
                df_date.rename(columns={"ts_code": "symbol", "amount": "voe"}, inplace=True)
                err = updb.update_stock(df_date, ignore_check)
                _log(2, TOTAL_PHASES, f"股票行情 {date_s}: {err} ({i+1}/{len(dates_id)})")
                if err != "OK":
                    break
            else:
                _log(2, TOTAL_PHASES, f"异常，{date_s}获取空数据")
                break
            if (i + 1) % 10 == 0:
                sl_time = 10 - time.time() + t0
                if sl_time > 0:
                    time.sleep(sl_time)
                t0 = time.time()

    # 3. 更新基础数据
    _log(3, TOTAL_PHASES, "开始更新基础数据")
    last_date_basic = updb.date_stock_basic()
    if last_date_basic is None or last_date_basic < today:
        df_date = pro.stock_basic(
            fields=["symbol", "name", "list_date", "industry", "act_name", "act_ent_type"])
        if len(df_date) > 0:
            err1 = updb.update_stock_basic(df_date)
            _log(3, TOTAL_PHASES, f"stock_basic_1: {err1}")
        df_date = pro.stock_company()
        df_date.rename(columns={"ts_code": "symbol"}, inplace=True)
        if len(df_date) > 0:
            err2 = updb.update_stock_basic(df_date)
            _log(3, TOTAL_PHASES, f"stock_basic_2: {err2}")
    else:
        _log(3, TOTAL_PHASES, "基础数据已是最新")
    _log(3, TOTAL_PHASES, "基础数据更新完成")

    # 4. 更新行情因子
    daily_basic_dates = updb.dates_await("stock_factor")
    updb.exist_stocks = []
    if not daily_basic_dates:
        _log(4, TOTAL_PHASES, "行情因子已是最新，无需更新")
    else:
        _log(4, TOTAL_PHASES, f"开始更新行情因子，共 {len(daily_basic_dates)} 个交易日待更新")
    fields = ["ts_code", "trade_date", "close", "turnover_rate",
              "turnover_rate_f", "volume_ratio", "pe", "pe_ttm",
              "pb", "ps", "ps_ttm", "dv_ratio", "dv_ttm",
              "total_share", "float_share", "free_share",
              "total_mv", "circ_mv", "limit_status"]
    t0 = time.time()
    for i, date in enumerate(daily_basic_dates):
        date_s = date.strftime('%Y%m%d')
        df_date = pro.daily_basic(trade_date=date_s, fields=fields)
        if len(df_date) > 0:
            df_date.rename(columns={"ts_code": "symbol"}, inplace=True)
            err = updb.update_stock_factor(df_date, ignore_check)
            _log(4, TOTAL_PHASES, f"行情因子 {date_s}: {err} ({i+1}/{len(daily_basic_dates)})")
            if err != "OK":
                break
        else:
            _log(4, TOTAL_PHASES, f"异常，{date_s}获取空数据")
            break
        if (i + 1) % 10 == 0:
            sl_time = 10 - time.time() + t0
            if sl_time > 0:
                time.sleep(sl_time)
            t0 = time.time()

    # 5. 更新业绩预告
    forecast_dates = updb.dates_await("stock_forecast")
    if not forecast_dates:
        _log(5, TOTAL_PHASES, "业绩预告已是最新，无需更新")
        updb.write_table_date("stock_forecast")
    else:
        _log(5, TOTAL_PHASES, f"开始更新业绩预告，共 {len(forecast_dates)} 个日期待更新")
    t0 = time.time()
    for i, date in enumerate(forecast_dates):
        date_s = date.strftime('%Y%m%d')
        df_date = pro.forecast(ann_date=date_s)
        if len(df_date) > 0:
            df_date.rename(columns={"ts_code": "symbol"}, inplace=True)
            err = updb.update_stock_forecast(df_date, date)
            _log(5, TOTAL_PHASES, f"业绩预告 {date_s}: {err} ({i+1}/{len(forecast_dates)})")
            if err != "OK":
                break
        else:
            _log(5, TOTAL_PHASES, f"{date_s}无业绩预告数据 ({i+1}/{len(forecast_dates)})")
        if (i + 1) % 10 == 0:
            sl_time = 10 - time.time() + t0
            if sl_time > 0:
                time.sleep(sl_time)
            t0 = time.time()

    # 6. 更新分红
    dividend_dates = updb.dates_await("stock_dividend")
    if not dividend_dates:
        _log(6, TOTAL_PHASES, "分红数据已是最新，无需更新")
        updb.write_table_date("stock_dividend")
    else:
        _log(6, TOTAL_PHASES, f"开始更新分红数据，共 {len(dividend_dates)} 个日期待更新")
    t0 = time.time()
    for i, date in enumerate(dividend_dates):
        date_s = date.strftime('%Y%m%d')
        df_date = pro.dividend(ex_date=date_s)
        if len(df_date) > 0:
            df_date.rename(columns={"ts_code": "symbol"}, inplace=True)
            err = updb.update_stock_dividend(df_date, date)
            _log(6, TOTAL_PHASES, f"分红 {date_s}: {err} ({i+1}/{len(dividend_dates)})")
            if err != "OK":
                break
        else:
            _log(6, TOTAL_PHASES, f"{date_s}无分红数据 ({i+1}/{len(dividend_dates)})")
        if (i + 1) % 10 == 0:
            sl_time = 10 - time.time() + t0
            if sl_time > 0:
                time.sleep(sl_time)
            t0 = time.time()

    # 7. 更新财务指标（逐只拉取，防止遗漏）
    HEARTBEAT_SEC = 30
    def _heartbeat_msg(i: int, total: int, t_start: float) -> str:
        elapsed = time.time() - t_start
        if i > 0:
            rate = i / elapsed
            eta = (total - i) / rate if rate > 0 else 0
            eta_m = int(eta // 60)
            eta_s = int(eta % 60)
            return f"财报拉取进度 {i}/{total}（{i*100//total}%） 已耗时 {int(elapsed//60)}m{int(elapsed%60)}s 预计剩余 {eta_m}m{eta_s}s"
        return f"财报拉取进度 0/{total}（0%）"

    report_dates = updb.dates_await("stock_report")
    if not report_dates:
        _log(7, TOTAL_PHASES, "财务指标已是最新，无需更新")
        updb.write_table_date("stock_report")
        return

    _log(7, TOTAL_PHASES, f"开始更新财务指标，共 {len(report_dates)} 个日期待汇总清单")
    all_stocks = set()
    _log(7, TOTAL_PHASES, f"财报清单汇总中，扫描 {len(report_dates)} 个披露日期...")
    t_phase7 = time.time()
    t0 = time.time()
    for i, date in enumerate(report_dates):
        diff_days = (today - date).days
        if diff_days > 275:
            continue
        date_s = date.strftime('%Y%m%d')
        try:
            df_date = pro.disclosure_date(actual_date=date_s)
            if len(df_date) > 0:
                codes = df_date['ts_code'].tolist()
                all_stocks.update(codes)
        except Exception as e:
            _log(7, TOTAL_PHASES, f"获取财报更新清单 {date_s} 失败：{str(e)}")
            return
        if (i + 1) % 10 == 0 or time.time() - t_phase7 > HEARTBEAT_SEC:
            _log(7, TOTAL_PHASES, f"财报清单汇总 {i+1}/{len(report_dates)}（已收集 {len(all_stocks)} 只股票）")
            t_phase7 = time.time()
        if (i + 1) % 10 == 0:
            sl_time = 10 - time.time() + t0
            if sl_time > 0:
                time.sleep(sl_time)
            t0 = time.time()

    stock_list = sorted(list(all_stocks))
    if not stock_list:
        _log(7, TOTAL_PHASES, "财报数据已是最新，无需更新")
        updb.write_table_date("stock_report")
        return

    _log(7, TOTAL_PHASES, f"财报清单汇总完成，待更新股票总数：{len(stock_list)} 只，开始拉取财务指标")
    result_list = []
    err_list = []
    t_start = time.time()
    last_log_time = t_start
    t_rate = t_start
    for i, code in enumerate(stock_list, 1):
        try:
            df = pro.fina_indicator(ts_code=code)
            if len(df) > 0:
                result_list.append(df)
        except Exception as e:
            err_list.append(code)
        now = time.time()
        if i % 10 == 0 or now - last_log_time > HEARTBEAT_SEC:
            _log(7, TOTAL_PHASES, _heartbeat_msg(i, len(stock_list), t_start))
            last_log_time = now
        if (i + 1) % 10 == 0:
            sl = 10 - (time.time() - t_rate)
            if sl > 0:
                time.sleep(sl)
            t_rate = time.time()

    if result_list:
        _log(7, TOTAL_PHASES, f"财务指标全部拉取完成！成功 {len(result_list)} 只（失败 {len(err_list)} 只），开始写入数据库")
        df = pd.concat(result_list, ignore_index=True)
        df.rename(columns={"ts_code": "symbol"}, inplace=True)
        err = updb.update_stock_report(df)
        _log(7, TOTAL_PHASES, f"财务指标写入: {err}（共 {len(df)} 条记录）")
    else:
        _log(7, TOTAL_PHASES, "未获取到任何财报数据")

    # 二次拉取失败股票
    if err_list:
        _log(7, TOTAL_PHASES, f"开始二次拉取 {len(err_list)} 只失败的股票")
        retry_list = list(err_list)
        err_list = []
        result_list = []
        t_start = time.time()
        last_log_time = t_start
        t0 = time.time()
        for i, code in enumerate(retry_list, 1):
            try:
                df = pro.fina_indicator(ts_code=code)
                if len(df) > 0:
                    result_list.append(df)
                else:
                    err_list.append(code)
            except Exception as e:
                err_list.append(code)
            now = time.time()
            if i % 5 == 0 or now - last_log_time > HEARTBEAT_SEC:
                _log(7, TOTAL_PHASES, f"二次拉取 {i}/{len(retry_list)}（成功 {len(result_list)} 失败 {len(err_list)}）")
                last_log_time = now
            if (i + 1) % 10 == 0:
                sl_time = 10 - time.time() + t0
                if sl_time > 0:
                    time.sleep(sl_time)
                t0 = time.time()
        if result_list:
            df = pd.concat(result_list, ignore_index=True)
            df.rename(columns={"ts_code": "symbol"}, inplace=True)
            err = updb.update_stock_report(df)
            _log(7, TOTAL_PHASES, f"二次读取财务指标写入: {err}（补录 {len(result_list)} 只）")
    if err_list:
        _log(7, TOTAL_PHASES, f"财报指标更新完成（最终失败 {len(err_list)} 只：{err_list[:8]}{'...' if len(err_list)>8 else ''}）")
    else:
        _log(7, TOTAL_PHASES, "财务指标全部更新完成！")


def example_baostock(DB_path: str = ''):
    if datetime.now().hour < 15:
        today = datetime.now().date() - timedelta(days=1)
    else:
        today = datetime.now().date()
    if today.weekday() == 6:
        today = today - timedelta(days=2)
    elif today.weekday() == 5:
        today = today - timedelta(days=1)
    today_s = today.strftime('%Y-%m-%d')
    updb = Updb(DB_path)

    lg = bs.login()
    if lg.error_code != '0':
        _log(1, 2, f'baostock login error: {lg.error_code} {lg.error_msg}')
    else:
        _log(1, 2, "baostock 登录成功")

    translate = {"date": "trade_date",
                 "code": "symbol",
                 "preclose": "pre_close",
                 "volume": "vol",
                 "amount": "voe"}
    id_list = ["sz.399001", "sh.000001"]
    for code in id_list:
        start_date = updb.date_stock_index(code)
        if start_date is None:
            start_date = today - timedelta(days=730)
        elif today <= start_date:
            continue
        rs = bs.query_history_k_data_plus(code,
            "date,code,open,high,low,close,preclose,volume,amount",
            start_date=start_date.strftime('%Y-%m-%d'),
            end_date=today_s,
            frequency="d")
        if rs.error_code != '0':
            _log(1, 2, f'baostock query error: {rs.error_code} {rs.error_msg}')
        data_list = []
        while (rs.error_code == '0') & rs.next():
            data_list.append(rs.get_row_data())
        df = pd.DataFrame(data_list, columns=rs.fields)
        if len(df) > 0:
            df.rename(columns=translate, inplace=True)
            df['vol'] = df['vol'].astype(float) / 100
            df['vol'] = df['vol'].round(2)
            df['voe'] = df['voe'].astype(float) / 1000
            df['voe'] = df['voe'].round(2)
            err = updb.update_stock_index(df)
            _log(1, 2, f"baostock 指数 {code}: {err}")
    bs.logout()
    _log(1, 2, "baostock 指数数据更新完成")


def example_tushare_120(api: str = '你的API', DB_path: str = '', ignore_check: bool = False):
    TOTAL_PHASES = 2
    if datetime.now().hour < 15:
        today = datetime.now().date() - timedelta(days=1)
    else:
        today = datetime.now().date()
    if today.weekday() == 6:
        today = today - timedelta(days=2)
    elif today.weekday() == 5:
        today = today - timedelta(days=1)

    today_s = today.strftime('%Y%m%d')
    updb = Updb(DB_path)
    pro = ts.pro_api(api)

    # 更新股票日线（仅此一项，指数由 baostock 负责）
    dates_id = updb.dates_await("stock")
    if not dates_id:
        _log(2, TOTAL_PHASES, "股票数据已是最新，无需更新")
    else:
        _log(2, TOTAL_PHASES, f"开始更新股票行情，共 {len(dates_id)} 个交易日待更新")
        t0 = time.time()
        for i, date in enumerate(dates_id):
            date_s = date.strftime('%Y%m%d')
            df_date = pro.daily(trade_date=date_s)
            if len(df_date) > 0:
                df_date.rename(columns={"ts_code": "symbol", "amount": "voe"}, inplace=True)
                err = updb.update_stock(df_date, ignore_check)
                _log(2, TOTAL_PHASES, f"股票行情 {date_s}: {err} ({i+1}/{len(dates_id)})")
                if err != "OK":
                    break
            else:
                _log(2, TOTAL_PHASES, f"异常，{date_s}获取空数据")
                break
            if (i + 1) % 10 == 0:
                sl_time = 10 - time.time() + t0
                if sl_time > 0:
                    time.sleep(sl_time)
                t0 = time.time()
    _log(2, TOTAL_PHASES, "OK")


# ========== 默认配置 ==========
def _get_default_option() -> dict:
    return {"db_path": os.path.join(os.path.dirname(__file__), "Test.duckdb"),
            "days": 730,
            "ex_do": True,
            "stock_index": "stock_index",
            "map_stock_index": {
                "trade_date": "trade_date",
                "symbol": "symbol",
                "open": "open",
                "high": "high",
                "low": "low",
                "close": "close",
                "pre_close": "pre_close",
                "vol": "vol",
                "voe": "voe"},
            "stock": "stock",
            "map_stock": {
                "trade_date": "trade_date",
                "symbol": "symbol",
                "open": "open",
                "high": "high",
                "low": "low",
                "close": "close",
                "pre_close": "pre_close",
                "vol": "vol",
                "voe": "voe"},
            "stock_basic": "stock_basic",
            "map_stock_basic": {
                "symbol": "symbol",
                "name": "name",
                "check": ["industry", "business_scope", "main_business", "province", "city", "act_ent_type", "concept"]},
            "stock_factor": "stock_factor",
            "map_stock_factor": {
                "symbol": "symbol",
                "trade_date": "trade_date"},
            "stock_forecast": "stock_forecast",
            "map_stock_forecast": {
                "symbol": "symbol",
                "ann_date": "ann_date"},
            "stock_dividend": "stock_dividend",
            "map_stock_dividend": {
                "symbol": "symbol",
                "ann_date": "ann_date",
                "ex_date": "ex_date"},
            "stock_report": "stock_report",
            "map_stock_report": {
                "symbol": "symbol",
                "ann_date": "ann_date"},
            "_": "_",
            "map__": {}
            }


# ========== 主入口 ==========
if __name__ == '__main__':
    # 1. 确保 DB_setting.json 存在
    option_path = os.path.join(os.path.dirname(__file__), "DB_setting.json")
    if not os.path.isfile(option_path):
        fd = _get_default_option()
        with open(option_path, "w", encoding="utf-8") as f:
            json.dump(fd, f, ensure_ascii=False)

    # 2. 读取数据库路径
    with open(option_path, 'r', encoding='utf-8') as f:
        config = json.load(f)
    db_path = config.get("db_path", "Test.duckdb")

    # 3. 读取 API（tushare token）
    api_file = os.path.join(os.path.dirname(__file__), "API_tushare.txt")
    if not os.path.exists(api_file):
        with open(api_file, 'w', encoding='utf-8') as f:
            f.write('')  # 创建空文件
    with open(api_file, 'r', encoding='utf-8') as f:
        api_token = f.read().strip()

    if not api_token:
        print(f"错误：未找到 tushare API token，请在 {api_file} 中填入您的 token。")
        sys.exit(1)

    print("开始更新数据库...")
    # 4. 仅120积分，简单更新行情，先用 baostock 更新指数，再用 tushare 更新股票日线
    # example_baostock(db_path)
    # example_tushare_120(api_token, db_path, ignore_check=False)

    # 4 2000积分以上，完整更新，用tushare完整更新
    example_tushare_2000(api_token, db_path, ignore_check=False)
    print("数据库更新完成！")