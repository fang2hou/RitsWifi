$app.strings = {
    "en": {
        "MAIN_TITLE": "RitsWiFi",
        "RESULT": "Result",
        "LOGIN": "Login",
        "LOGOUT": "Logout",
        "SUCCESS": "Success!",
        "FAIL": "Fail!"
    },
    "zh-Hans": {
        "MAIN_TITLE": "立命馆 WiFi 助手",
        "RESULT": "结果",
        "LOGIN": "登入",
        "LOGOUT": "登出",
        "SUCCESS": "成功！",
        "FAIL": "失败！"
    },
    "zh-Hant": {
        "MAIN_TITLE": "立命館 WiFi 助理",
        "RESULT": "結果",
        "LOGIN": "登入",
        "LOGOUT": "登出",
        "SUCCESS": "成功！",
        "FAIL": "失敗！"
    },
    "ja": {
        "MAIN_TITLE": "RitsWiFi",
        "RESULT": "結果",
        "LOGIN": "ログイン",
        "LOGOUT": "ログアウト",
        "SUCCESS": "成功！",
        "FAIL": "失敗！"
    }
}

$ui.render({
    props: {
        title: $l10n("MAIN_TITLE")
    },
    views: [{
        type: "button",
        props: {
            title: $l10n("LOGIN")
        },
        layout: function(make, view) {
            make.width.equalTo(120)
            make.right.equalTo(view.mas_centerX).offset(-5)
            make.top.offset(10)
        },
        events: {
            tapped: function(sender) {
                $http.request({
                    method: "POST",
                    url: "https://webauth.ritsumei.ac.jp/login.html",
                    form: {
                        username: "is1234ab",
                        password: "12345678",
                        buttonClicked: "4",
                        redirect_url: "",
                        err_flag: "0"
                    },
                    handler: function(resp) {
                        if (resp.data.search("login_success") != -1) {
                            $ui.alert({
                                title: $l10n("RESULT"),
                                message: $l10n("SUCCESS")
                            })
                        } else {
                            $ui.alert({
                                title: $l10n("RESULT"),
                                message: $l10n("FAIL")
                            })
                        }
                    }
                })
            }
        }
    }, {
        type: "button",
        props: {
            title: $l10n("LOGOUT")
        },
        layout: function(make, view) {
            make.width.equalTo(120)
            make.left.equalTo(view.mas_centerX).offset(5)
            make.top.offset(10)
        },
        events: {
            tapped: function(sender) {
                $http.request({
                    method: "POST",
                    url: "https://webauth.ritsumei.ac.jp/logout.html",
                    form: {
                        userStatus: "1",
                        err_msg: "",
                        err_flag: "0"
                    },
                    handler: function(resp) {
                        if (resp.data.search("To complete the log off process") != -1) {
                            $ui.alert({
                                title: $l10n("RESULT"),
                                message: $l10n("SUCCESS")
                            })
                        } else {
                            $ui.alert({
                                title: $l10n("RESULT"),
                                message: $l10n("FAIL")
                            })
                        }
                    }
                })
            }
        }
    }, ]
})