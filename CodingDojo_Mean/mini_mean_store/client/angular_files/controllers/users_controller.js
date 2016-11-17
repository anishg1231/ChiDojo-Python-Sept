;function () {
  console.log('angular users controller loaded');
  'use strict'

  angular
    .module('myApp')
    .controller('usersController', Controller)

  function Controller() {
    var self =  this
    self.login = function () {
      console.log(self.logUser);
      usersFactory.login(self.logUser,function (returnData) {
        console.log('in callback', returnData);
        if (returnData.status){
          $location.url('/polls')
        }
        else {
            alert('bad login')
        }
      })
    }
      self.logout = function () {
        usersFactory.logout(function () {
          $location.url('/')
        })
      }
      function getSession() {
        usersFactory.getSession(function (data) {
          console.log(data);
          if (data.status) {
            self.myUser = {}
            self.myUser.name = data.name
            self.myUser.user_id = data._id
            $location.url('/polls')
          }
          else {
            $location.url('/')
          }
        })
      }
      getSession()
  }
}()
