# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st

if st.sidebar.button("홈"):
    st.switch_page("Hello.py")
if st.sidebar.button("연구원 수 분포"):
    st.switch_page("charts/rnd_population.py")
if st.sidebar.button("과학기술혁신 역량평가지수"):
    st.switch_page("charts/r_costii.py")
if st.sidebar.button("총 연구개발비 추이"):
    st.switch_page("charts/rnd_money.py")