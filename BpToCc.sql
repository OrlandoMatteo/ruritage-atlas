SELECT BestPractice.BPName,RoleModel.Name, SIA.SIA, CrossCutting.CCName
 FROM BestPractice
 LEFT JOIN BPtoCC ON BestPractice.idBestPractice = BPtoCC.idBP
 LEFT JOIN CrossCutting ON BPtoCC.idCC = CrossCutting.idCrossCutting
 LEFT JOIN SIA ON BestPractice.idSIA = SIA.idSIA
 LEFT JOIN RoleModel ON BestPractice.idRM = RoleModel.idRoleModel
 where CrossCutting.idCrossCutting in (1,2,3,4,5,6,7,8,9,10,11)
 AND SIA.SIA IN ('Migration') ;