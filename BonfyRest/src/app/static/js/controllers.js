function TaskList($scope,$http) {

	$http.get('/todo/api/v1.0/tasks').success(function(data) {
			//alert(data.tasks)
		    $scope.tasks = data.tasks;
		  });

	$scope.showAppPanel = function()
	{		
		$scope.AddAppPanelShow = true;
	};

	/** 添加App **/
	$scope.addTask = function()
	{
		var strArr = [];
		for(var key in $scope.task)
			strArr.push(key + ' : "' + $scope.task[key] + '"');
		
		$scope.AddAppPanelShow = false; // 
		alert(strArr.join(','));


	};


	$scope.login = function(task){
            $http.post("/todo/api/v1.0/tasks",task).success(function(data, status, headers, config){
                alert("success");
                alert(data.task);
            }).error(function(data, status, headers, config){
                alert("error");
            })
        }

    $scope.delete = function(task_id){
        
            $http.delete("/todo/api/v1.0/tasks/"+task_id).success(function(data, status, headers, config){
                alert("你已经成功删除");
            }).error(function(data, status, headers, config){
                alert("error");
            })
        
        //alert(task_id);
        }

    /*貌似这个不能搞，因为 没有 method：post*/
    $scope.login1 = function(task){
            $http({url:"/todo/api/v1.0/tasks",data:task}).success(function(data, status, headers, config){
                alert("success");
                alert(data.task);
            }).error(function(data, status, headers, config){
                alert("error");
            })
        }

    
/*	
  $scope.tasks = [
   {
        'id': 1,
        'title': 'Buy groceries',
        'description': 'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': false
    },
    {
        'id': 2,
        'title': 'Learn Python',
        'description': 'Need to find a good Python tutorial on the web',
        'done': true
    }
  ];
*/
}
