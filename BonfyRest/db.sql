USE [mine]
GO
/****** Object:  Table [dbo].[Task]    Script Date: 09/11/2014 10:07:47 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Task](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[title] [nvarchar](50) COLLATE Chinese_PRC_CI_AS NULL,
	[description] [nvarchar](300) COLLATE Chinese_PRC_CI_AS NULL,
	[done] [bit] NULL,
 CONSTRAINT [PK_Task] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (IGNORE_DUP_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
