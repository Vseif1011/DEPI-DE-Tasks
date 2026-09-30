insert into userData (Name,Password) values ('Seif', '12345678')
insert into userData (Name,Password) values ('Ahmed', '12345671')
insert into userData (Name,Password) values ('Nabil', '12345672')
insert into userData (Name,Password) values ('Youssef', '12345673')
insert into userData (Name,Password) values ('Joe', '12345674')
insert into userData (Name,Password) values ('Mazen', '12345676')

alter proc checkUserInfo (@userName nvarchar(50), @userPassword nvarchar(50)) 
as
begin
	declare @date date = getdate()
	declare @status nvarchar(50)
	if exists (
	select * 
	from userData
	where Name = @userName and Password = @userPassword 
	) 
	begin 
	  print 'User Found'
	  set @status = 'Success'
	  insert into LogTable (userName,userPassword,loginDate,loginStatus) values (@userName,@userPassword,@date,@status) 
	end
	else 
	begin 
	  print 'User not Found'
	  insert into LogTable (userName,userPassword,loginDate,loginStatus) values (@userName,@userPassword,@date,@status) 
	end
	select *
	from LogTable
end 

exec checkUserInfo 'Seif','12345678'
