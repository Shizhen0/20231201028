# 学生信息展示系统

## 项目简介
这是一个学生信息展示系统，包含Django后端和HTML前端页面。

## 项目结构
```
20231201028/
├── .gitignore          # Git忽略文件
├── README.md           # 项目说明文档
├── requirements.txt    # Python依赖包
├── manage.py          # Django管理脚本
├── mysite/            # Django项目配置
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── hello/             # Django应用
│   ├── views.py
│   ├── urls.py
│   └── apps.py
├── templates/         # 模板文件
│   └── hello/
│       └── index.html
├── student_info.html              # 学生信息页面（完整版）
├── student_info_clean.html        # 学生信息页面（纯净版）
├── student_info_fixed.html        # 学生信息页面（修复版）
├── student_info_isolated.html    # 学生信息页面（隔离版）
└── simple_student_info.html      # 学生信息页面（极简版）
```

## 功能特点
- 学生信息展示（学号：20231201028，姓名：石珍，班级：医学信息工程2023）
- 响应式设计，支持各种设备
- 现代化UI界面
- 无外部依赖，可直接在浏览器中打开

## 使用方法

### 1. 直接打开HTML文件
双击任意HTML文件即可在浏览器中查看学生信息：
- `simple_student_info.html` - 极简版本（推荐）
- `student_info_isolated.html` - 完整美观版本

### 2. 运行Django项目（需要Python环境）
```bash
# 安装依赖
pip install -r requirements.txt

# 运行数据库迁移
python manage.py migrate

# 启动开发服务器
python manage.py runserver

# 访问 http://127.0.0.1:8000/hello/
```

## GitHub同步步骤

### 第一步：安装Git
1. 访问 https://git-scm.com/downloads
2. 下载并安装Git for Windows
3. 安装时勾选"Add Git to PATH"选项

### 第二步：配置Git
```bash
# 设置用户名
git config --global user.name "你的GitHub用户名"

# 设置邮箱
git config --global user.email "你的GitHub邮箱"
```

### 第三步：初始化Git仓库
```bash
# 进入项目目录
cd C:\Users\shizh\Desktop\20231201028

# 初始化Git仓库
git init

# 添加所有文件
git add .

# 提交更改
git commit -m "初始提交：学生信息展示系统"
```

### 第四步：连接到GitHub
```bash
# 在GitHub上创建新仓库（不要初始化README）
# 然后执行以下命令：

git remote add origin https://github.com/你的用户名/你的仓库名.git
git branch -M main
git push -u origin main
```

## 注意事项
- 如果遇到CORS错误，请使用`simple_student_info.html`文件
- Django项目需要Python 3.9+环境
- 首次运行Django项目需要执行数据库迁移

## 技术支持
如有问题，请检查：
1. Python环境是否正确安装
2. 浏览器缓存是否已清除
3. 文件路径是否正确