# import torch
import torch.nn as nn


class CoconutFeatureExtract(nn.Module):
    def __init__(self,
                 input_size=768,
                 drop_out_rate=0.1,
                 num_of_classes=9292,
                 feature_size=192):
        super(CoconutFeatureExtract, self).__init__()
        self.input_size = input_size
        self.drop_out_rate = drop_out_rate
        self.num_of_classes = num_of_classes
        self.feature_size = feature_size
        self.use_batch = False
        self.create_params()
        return

    def create_params(self):
        self.dropout = nn.Dropout(self.drop_out_rate)
        self.bn = nn.BatchNorm1d(self.input_size)
        self.tanh = nn.Tanh()
        self.features = nn.Linear(self.input_size, self.feature_size)
        self.classfiy = nn.Linear(self.feature_size, self.num_of_classes, bias=False)
        self.reset_params()
        return

    def batch(self, use_batch):
        return

    def reset_params(self):
        for m in self.modules():
            if isinstance(m, nn.Linear):
                nn.init.xavier_uniform_(m.weight)

    def forward(self, input_tensor):
        last_hidden_state, pooled_output, hidden_states, attentions = input_tensor
        pooled_output = self.dropout(pooled_output)
        out = self.bn(pooled_output)
        out = self.tanh(out)
        features = self.features(out)
        out = self.classfiy(features)
        return features, out
