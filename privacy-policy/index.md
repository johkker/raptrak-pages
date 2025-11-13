# Política de Privacidade - RapTrak

**Última atualização:** 13 de novembro de 2025

## 1. Introdução

O RapTrak é um aplicativo mobile dedicado a conectar a comunidade de batalhas de rap no Brasil. Esta Política de Privacidade descreve como coletamos, usamos, armazenamos e protegemos suas informações pessoais.

Ao usar nosso aplicativo, você concorda com os termos desta política.

## 2. Dados que Coletamos

### 2.1 Dados de Cadastro
Quando você cria uma conta, coletamos:
- **Nome completo**
- **E-mail**
- **Senha** (armazenada com criptografia bcrypt)
- **CPF** (para verificação de identidade)
- **Data de nascimento** (para verificar idade mínima de 14 anos)
- **Nome artístico** (opcional, para usuários do tipo "rapper")
- **Avatar/foto de perfil** (opcional)
- **Tipos de usuário** (comum, rapper, administrador de local, beatmaker)
- **Cidade** (opcional)
- **Biografia** (opcional)
- **Redes sociais** (opcional)

### 2.2 Login com Google
Se você optar por fazer login com sua conta Google, coletamos:
- **E-mail** da sua conta Google
- **Nome** cadastrado no Google
- **Foto de perfil** do Google

**Importante:** Quando você usa o Google Sign-In, suas credenciais do Google nunca são compartilhadas conosco. Recebemos apenas um token de autenticação validado pelo Google que contém as informações acima.

### 2.3 Dados de Localização
Coletamos dados de localização **apenas quando você usa recursos específicos**:
- Busca de batalhas próximas a você
- Visualização de batalhas no mapa
- Criação ou edição de endereços de batalhas

**A localização não é armazenada permanentemente**. Utilizamos a localização apenas para fornecer os serviços solicitados e descartamos esses dados após o uso, instantaneamente.

**Você pode desativar o acesso à localização** nas configurações do seu dispositivo. Isso limitará algumas funcionalidades do app.

### 2.4 Dados de Atividade na Plataforma
- Batalhas que você cria ou descobre
- Batalhas que você gerencia (como administrador)
- Troféus que você recebe
- Solicitações de propriedade de batalhas
- Curtidas em batalhas
- Estatísticas de participação (para usuários "rapper")

### 2.5 Dados Técnicos
- **Token de autenticação JWT** (válido por 24 horas)
- Informações de erro e logs para melhoria do aplicativo

## 3. Como Usamos Seus Dados

Utilizamos suas informações para:
- **Autenticar sua identidade** e gerenciar sua conta
- **Exibir batalhas próximas** à sua localização
- **Conectar você com outras batalhas e usuários**
- **Permitir que você gerencie batalhas** (como administrador)
- **Atribuir troféus e reconhecimentos**
- **Processar solicitações de propriedade** de batalhas
- **Melhorar a segurança** e prevenir fraudes
- **Analisar e melhorar** nossos serviços
- **Cumprir obrigações legais**

## 4. Compartilhamento de Dados

### 4.1 Informações Públicas
As seguintes informações são **visíveis para outros usuários** do aplicativo:
- Nome artístico (se fornecido)
- Avatar/foto de perfil
- Biografia e cidade
- Troféus recebidos
- Batalhas que você administra
- Estatísticas de participação (para rappers)

### 4.2 Informações Privadas
**Nunca compartilhamos publicamente:**
- Seu CPF
- Sua data de nascimento completa
- Seu e-mail
- Sua senha
- Sua localização exata

### 4.3 Serviços de Terceiros
Utilizamos os seguintes serviços de terceiros:
- **Google Sign-In** - para autenticação (sujeito à [Política de Privacidade do Google](https://policies.google.com/privacy))
- **Google Maps API** - para exibição de mapas e geolocalização de endereços
- **Provedores de hospedagem** - para armazenar dados da aplicação

**Não vendemos ou alugamos seus dados pessoais para terceiros.**

### 4.4 Exigências Legais
Podemos divulgar suas informações se:
- Exigido por lei ou ordem judicial
- Necessário para proteger nossos direitos legais
- Detectarmos fraude ou atividade ilegal
- For necessário para proteger a segurança de usuários

## 5. Segurança dos Dados

Implementamos medidas de segurança para proteger suas informações:
- **Senhas criptografadas** com algoritmo bcrypt
- **Tokens JWT** com expiração de 24 horas
- **Conexões HTTPS** para toda comunicação entre app e servidor
- **Banco de dados PostgreSQL** com controles de acesso
- **Validação de dados** em todas as entradas de usuário

Apesar de todos os esforços, nenhum sistema é 100% seguro. Recomendamos que você:
- Use uma senha forte e única
- Não compartilhe suas credenciais de acesso
- Faça logout ao usar dispositivos compartilhados

## 6. Seus Direitos (LGPD)

De acordo com a Lei Geral de Proteção de Dados (LGPD), você tem direito a:
- **Confirmar** a existência de tratamento dos seus dados
- **Acessar** seus dados pessoais
- **Corrigir** dados incompletos, inexatos ou desatualizados
- **Solicitar anonimização, bloqueio ou eliminação** de dados desnecessários
- **Solicitar portabilidade** dos seus dados
- **Revogar consentimento** a qualquer momento
- **Excluir sua conta** e todos os dados associados

### Como Exercer Seus Direitos
Para exercer qualquer um desses direitos, entre em contato conosco através do e-mail: **lgpd@raptrak.me**

## 7. Exclusão de Conta

Você pode excluir sua conta a qualquer momento através do menu **Configurações > Excluir Conta** no aplicativo.

Quando você exclui sua conta:
- Seus dados pessoais (nome, e-mail, CPF, senha) são **permanentemente removidos**
- Seu nome artístico pode ser mantido em registros históricos de troféus (anonimizado)
- Batalhas que você criou continuam no sistema (com seu vínculo removido)
- Troféus concedidos por você são mantidos para integridade histórica

## 8. Retenção de Dados

Mantemos seus dados enquanto sua conta estiver ativa ou conforme necessário para:
- Fornecer nossos serviços
- Cumprir obrigações legais
- Resolver disputas
- Fazer cumprir nossos acordos

Após exclusão da conta, dados pessoais identificáveis são removidos em até **30 dias**.

## 9. Menores de Idade

O RapTrak exige idade mínima de **14 anos** para uso. Verificamos a idade através da data de nascimento fornecida no cadastro.

Se identificarmos que um usuário menor de 14 anos criou uma conta, ela será imediatamente desativada e os dados excluídos.

## 10. Cookies e Armazenamento Local

O aplicativo mobile RapTrak utiliza:
- **AsyncStorage** (React Native) para armazenar:
  - Token de autenticação JWT
  - Dados básicos do usuário (para acesso offline)
  - Preferências do aplicativo

**Não utilizamos cookies de rastreamento ou publicidade.**

## 11. Transferência Internacional de Dados

**Importante:** Seus dados pessoais são armazenados em servidores que podem estar localizados fora do Brasil.

De acordo com a LGPD (Art. 33), realizamos transferência internacional de dados com base nas seguintes garantias:

- **Países com nível adequado de proteção:** Priorizamos provedores em países reconhecidos pela ANPD como tendo proteção adequada de dados
- **Cláusulas contratuais:** Mantemos contratos com cláusulas padrão de proteção de dados com nossos provedores de hospedagem
- **Certificações internacionais:** Utilizamos provedores com certificações de segurança reconhecidas (ISO 27001, SOC 2, etc.)
- **Compromisso de conformidade:** Nossos provedores são obrigados contratualmente a seguir os princípios da LGPD

Você tem o direito de solicitar informações específicas sobre onde seus dados estão armazenados e quais medidas de proteção estão sendo aplicadas.

## 12. Alterações nesta Política

Podemos atualizar esta Política de Privacidade periodicamente. Quando houver mudanças significativas:
- Atualizaremos a data de "Última atualização"
- Notificaremos você através do aplicativo ou e-mail
- Solicitaremos seu consentimento quando exigido por lei

O uso continuado do aplicativo após as mudanças constitui aceitação da política atualizada.

## 13. Base Legal para Tratamento (LGPD)

Processamos seus dados com base em:
- **Consentimento:** Para coleta de localização e dados opcionais
- **Execução de contrato:** Para fornecer os serviços do aplicativo
- **Cumprimento de obrigação legal:** Para verificação de idade (14+) e identificação (CPF)
- **Legítimo interesse:** Para segurança, prevenção de fraudes e melhoria dos serviços

## 14. Contato e Encarregado de Dados

Para questões sobre privacidade, exercício de direitos ou dúvidas sobre esta política:

**E-mail:** johkker@gmail.com

Você também pode registrar uma reclamação junto à **Autoridade Nacional de Proteção de Dados (ANPD)**: https://www.gov.br/anpd/pt-br

## 15. Consentimento

Ao criar uma conta e usar o RapTrak, você declara que:
- Leu e compreendeu esta Política de Privacidade
- Tem pelo menos 14 anos de idade
- Concorda com a coleta, uso e compartilhamento de dados conforme descrito
- Autoriza o tratamento dos seus dados pessoais para as finalidades indicadas

---

**RapTrak** - Conectando a comunidade de batalhas de rap  
Versão 1.0.0
