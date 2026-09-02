---
name: fliggy-travel
display_name: 飞猪旅行
description: 飞猪旅行全品类搜索——酒店/机票/火车票/景点门票/万豪/美食/交通/行程规划，9大功能全覆盖，零配置即装即用，数据来自飞猪官方API
version: 2.0.0
author: mako2026
license: MIT-0
tags:
  - travel
  - hotel
  - flight
  - train
  - fliggy
  - 飞猪
  - 旅行
  - 门票
tools:
  - name: fliggyTravelPlan
    description: 行程规划，用自然语言描述旅行需求，智能推荐含交通住宿景点的行程方案
    primaryEnv: FLYAI_PROXY_URL
    env:
      - name: FLYAI_PROXY_URL
        description: 飞猪代理URL（自动配置，无需手动设置）
        required: false
      - name: PROXY_TOKEN
        description: 代理认证Token（自动配置，无需手动设置）
        required: false
    parameters:
      - name: query
        type: string
        description: 旅行需求，自然语言，如"三亚5天亲子游"、"周末杭州2日游"
        required: true
  - name: fliggyFastSearch
    description: 极速搜索，快速搜索飞猪全品类产品
    parameters:
      - name: query
        type: string
        description: 搜索关键词，如"上海迪士尼门票"、"北京到上海机票"
        required: true
  - name: fliggyHotelSearch
    description: 搜索飞猪酒店，返回酒店列表含价格、评分和预订链接
    parameters:
      - name: destination
        type: string
        description: 目的地城市，如"上海"、"北京"
        required: true
      - name: extra
        type: string
        description: 补充信息，如"外滩附近 明天入住"
        required: false
  - name: fliggyFlightSearch
    description: 机票查询，查国内航班实时票价、航班号和起降时间
    parameters:
      - name: origin
        type: string
        description: 出发地城市，如"北京"
        required: true
      - name: destination
        type: string
        description: 目的地城市，如"上海"
        required: false
      - name: depDate
        type: string
        description: 出发日期，格式YYYY-MM-DD
        required: false
      - name: backDate
        type: string
        description: 回程日期，格式YYYY-MM-DD
        required: false
      - name: seatClass
        type: string
        description: 舱位等级，如经济舱、公务舱
        required: false
      - name: directOnly
        type: boolean
        description: 是否只看直飞
        required: false
  - name: fliggyTrainSearch
    description: 火车票查询，查高铁/动车/火车票余票价格和时刻表
    parameters:
      - name: origin
        type: string
        description: 出发地城市，如"北京"
        required: true
      - name: destination
        type: string
        description: 目的地城市，如"上海"
        required: false
      - name: depDate
        type: string
        description: 出发日期，格式YYYY-MM-DD
        required: false
      - name: seatClass
        type: string
        description: 座位等级，如商务座、一等座、二等座
        required: false
      - name: trainType
        type: string
        description: 车型，如高铁、动车、火车
        required: false
      - name: onlyHasStock
        type: boolean
        description: 是否只看有票
        required: false
  - name: fliggyPoiSearch
    description: 景点门票搜索，查景点门票价格、评分和预订链接
    parameters:
      - name: destination
        type: string
        description: 目的地城市，如"北京"
        required: true
      - name: keyword
        type: string
        description: 景点关键词，如"迪士尼"
        required: false
  - name: fliggyMarriottHotelSearch
    description: 万豪酒店搜索，搜万豪集团旗下酒店含价格和预订链接
    parameters:
      - name: destination
        type: string
        description: 目的地城市，如"上海"
        required: true
      - name: extra
        type: string
        description: 补充信息，如"行政酒廊"
        required: false
  - name: fliggyMarriottHotelDetail
    description: 万豪酒店详情，获取单个万豪酒店的详细信息和房型
    parameters:
      - name: hotelId
        type: string
        description: 酒店ID，从搜索结果获取
        required: true
  - name: fliggyMarriottPackageSearch
    description: 万豪套餐搜索，搜万豪酒店套餐产品
    parameters:
      - name: destination
        type: string
        description: 目的地城市，如"三亚"
        required: true
      - name: extra
        type: string
        description: 补充信息，如"亲子套餐"
        required: false
  - name: fliggyFoodSearch
    description: 美食推荐，推荐目的地周边美食餐厅含评分和人均
    parameters:
      - name: destination
        type: string
        description: 目的地/地标，如"上海外滩"
        required: true
      - name: keyword
        type: string
        description: 美食类型，如"火锅"
        required: false
  - name: fliggyTransportSearch
    description: 市内交通，查询城市内两地公交/地铁路线
    parameters:
      - name: origin
        type: string
        description: 出发地，如"上海虹桥站"
        required: true
      - name: destination
        type: string
        description: 目的地，如"外滩"
        required: true
      - name: city
        type: string
        description: 所在城市，如"上海"
        required: false
---

# 飞猪旅行

飞猪旅行全品类搜索技能，覆盖酒店、机票、火车票、景点门票、万豪酒店、美食推荐、市内交通、行程规划9大品类。数据来自飞猪旅行官方API，价格真实、带预订链接。

## ✅ 能做什么

| 功能 | 说明 |
|------|------|
| 🗺 行程规划 | 自然语言描述需求，智能生成含交通住宿景点的完整行程 |
| 🏨 酒店搜索 | 按城市/区域/星级查酒店，返回价格/评分/预订链接 |
| ✈️ 机票查询 | 查国内航班价格/时刻/航司，支持单程往返 |
| 🚄 火车票查询 | 查高铁/动车/普速车次余票、票价和坐席 |
| 🎫 景点门票 | 查景点门票价格和预订链接 |
| 🏢 万豪酒店 | 万豪集团酒店搜索、详情、套餐 |
| 🍜 美食推荐 | 周边美食餐厅推荐，含评分人均地址 |
| 🚇 市内交通 | 公交/地铁路线查询，含打车参考 |
| ⚡ 极速搜索 | 全品类快速检索 |

## ⚠️ 不能做什么

- 不支持在线下单/支付，预订链接跳转飞猪APP或网页完成
- 日期请用自然语言或YYYY-MM-DD格式描述

## 🔒 数据安全

所有查询通过云端代理转发，飞猪API密钥仅存储在服务端，客户端零密钥，保障数据安全。代理不存储用户数据。

## 💡 使用提示

- 酒店搜索支持补充区域、星级、日期，如`extra="外滩附近 明天入住"`
- 机票搜索可筛选舱位和直飞，如`seatClass="经济舱", directOnly=true`
- 行程规划支持复杂需求，如`query="三亚5天亲子游 预算1万"`
