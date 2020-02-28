Page({
  data: {},
  onLoad: function () {
  },
  getPhoneNumber: function (e) {
    wx.login({
      success: res => {
        wx.showLoading({
          title: '登陆中',
        });
        wx.request({
          url:  'https://your-domain/wx_register',
          data: {
            code: res.code,
            encryptedData: e.detail.encryptedData,
            iv: e.detail.iv
          },
          method: 'GET',
          success: function (res) {
            wx.hideLoading();
            if (res.statusCode == 201) {
            }
            else {
              //handle the error
            }
          },
          fail: function (err) {
            wx.hideLoading();
              //handle the error
          }
        })
      }
    })
  }
});