function bindCaptchaBtnClick() {
   $("#captcha-btn").on("click", function (event) {
       $this = $(this);
       var email = $("input[name='email']").val();
       if (!email){
           alert("请先输入邮箱！！")
           return;
       }
       // 通过js发送网络请求
       $.ajax({
           url: "/user/captcha",
           method: "POST",
           data: {
               "email": email
           },
           success: function (res) {
               var code = res["code"];
               // alert(code);
               if (code === 200){
                   // 取消点击事件
                   $this.off("click");
                   // 开始倒计时
                   var countDown = 60;
                   var timer = setInterval(function () {
                       countDown -= 1;
                       if (countDown > 0){
                           $this.text(countDown+"秒后重新发送")
                       }else{
                           $this.text("获取验证码");
                           // 重新绑定事件
                           bindCaptchaBtnClick();
                           // 清除倒计时，否则一直执行下去；
                           clearInterval(timer);
                       }
                   }, 1000);
                   alert("验证码发送成功");
               }else{
                   alert(res["message"]);
               }
           }
       })
   })
}


// 等网页文档所有元素都加载完成后执行
$(function () {
    bindCaptchaBtnClick()
});
