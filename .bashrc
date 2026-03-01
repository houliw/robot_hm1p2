alias update='sudo apt update && sudo apt upgrade -y'  # 一键更新系统
alias install='sudo apt install -y'                    # 安装软件（自动确认）
alias remove='sudo apt remove -y'                      # 卸载软件
alias search='apt search'                              # 搜索软件包

alias gs='git status'         # 查看工作区状态
alias ga='git add'            # 添加文件到暂存区（用法：ga 文件名）
alias gc='git commit -m'      # 提交并添加备注（用法：gc "提交信息"）
alias gp='git push'           # 推送到远程仓库
alias gl='git log --oneline'  # 简洁显示提交历史
alias gco='git checkout'      # 切换分支或恢复文件
alias gb='git branch'         # 列出所有分支